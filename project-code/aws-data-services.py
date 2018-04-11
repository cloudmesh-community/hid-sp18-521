import boto3, smart_open, pprint, pymysql, urllib, json, decimal, psycopg2, yaml
from boto3.dynamodb.conditions import Key, Attr

with open ("etc/aws-data-services.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

mysql_user = config['cloudmesh']['aws-data-services']['mysql']['user']['name']
mysql_password = config['cloudmesh']['aws-data-services']['mysql']['user']['password']
redshift_user = config['cloudmesh']['aws-data-services']['redshift']['user']['name']
redshift_password = config['cloudmesh']['aws-data-services']['redshift']['user']['password']
# ACCESS_KEY_ID = config['cloudmesh']['aws-data-services']['aws']['ACCESS_KEY_ID']
# SECRET_ACCESS_KEY = config['cloudmesh']['aws-data-services']['aws']['SECRET_ACCESS_KEY']

# S3 bucket name = hid-sp18-521

# https://data.medicare.gov/Hospital-Compare/Patient-survey-HCAHPS-Hospital/dgck-syfz

# Pulls Medicare hospital survey data set in CSV format directly from their web site into an S3 bucket
def medicare_patient_survey_data_csv_to_s3():
    with smart_open.smart_open('s3://' + ACCESS_KEY_ID + ':' + SECRET_ACCESS_KEY +'@hid-sp18-521/PatientSurveyData.csv', 'wb') as fout:
        for line in smart_open.smart_open('https://data.medicare.gov/resource/rmgi-5fhi.csv'):
            response = fout.write(line + '\n')
            return response

medicare_patient_survey_data_csv_to_s3()

# Pulls Medicare patient survey data set in JSON format directly from their web site into an S3 bucket
def medicare_patient_survey_data_json_to_s3():
    with smart_open.smart_open('s3://' + ACCESS_KEY_ID + ':' + SECRET_ACCESS_KEY +'@hid-sp18-521/PatientSurveyData.json', 'wb') as fout:
        for line in smart_open.smart_open('https://data.medicare.gov/resource/rmgi-5fhi.json'):
            response = fout.write(line + '\n')
            return response

# Pulls a list of all of the files that exist in the bucket this application uses
def s3_bucket_allfiles():
    file_names = []

    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    bucket = s3.Bucket('hid-sp18-521')

    for object in bucket.objects.all():
        file_names.append(object.key)

    return file_names

# Import S3 File into RDS using AWS Data Pipeline (show how it was created and how it can be called from here)
def data_pipeline_s3_to_rds():
    pipeline = boto3.client('datapipeline', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    response = pipeline.activate_pipeline(pipelineId='df-09855991V8LTRRRNJOQW')

    return response

# Return the runtime status of the S3 to RDS data pipelines
def data_pipeline_s3_to_rds_status():
    pipeline = boto3.client('datapipeline', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    pipeline_status = pipeline.describe_pipelines(pipelineIds=['df-09855991V8LTRRRNJOQW'])

    fields = pipeline_status['pipelineDescriptionList'][0]['fields']

    for field in fields:
        if field['key'] == '@pipelineState':
            return field['stringValue']

# Query the table that contains the data we imported into MySQL on RDS from S3
def query_mysql_data():
    connection = pymysql.connect(host='iu-sp18.cgnrvgmckfic.us-east-1.rds.amazonaws.com',
                                 user=mysql_user,
                                 password=mysql_password,
                                 db='I524',
                                 charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    sql = "SELECT * FROM PatientSurveyData" #TODO: Change this to something useful
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# Delete the DynamoDB table PatientSurveyData
def dynamodb_delete_table():
    dynamodb = boto3.client('dynamodb', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    response = dynamodb.delete_table(TableName='PatientSurveyData')

    return response

# Create the DynamoDB table PatientSurveyData
def dynamodb_create_table():
    dynamodb = boto3.client('dynamodb', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    response = dynamodb.create_table(TableName='PatientSurveyData',
                                  KeySchema=[{'AttributeName': 'provider_id', 'KeyType': 'HASH'}, ],
                                  AttributeDefinitions=[{'AttributeName': 'provider_id', 'AttributeType': 'S'}],
                                  ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5},
                                  )
    return response

#Import JSON file from web and into DynamoDB table
def dynamodb_insert_json_file():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    table = dynamodb.Table('PatientSurveyData')

    url = "https://data.medicare.gov/resource/rmgi-5fhi.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read(), parse_float=decimal.Decimal)

    for row in data:
        response = table.put_item(Item=row)

    return response

# Query the data set we just inserted into DymamoDB (Get all hospitals from the survey located in Missouri)
def dynamodb_query_data():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    table = dynamodb.Table('PatientSurveyData')

    response = table.scan(FilterExpression=Attr('state').eq('MO'))

    items = response['Items']

    return items

# Import CSV data into Redshift cluster from S3 CSV file (created in Management Console and SQL Workbench J)
def redshift_load_table_from_s3():
    redshift = psycopg2.connect(dbname= 'i524', host='iu-sp18.c9tuimcojmsj.us-east-1.redshift.amazonaws.com',
                                port= '5439', user= redshift_user, password= redshift_password)

    cur = redshift.cursor()

    cur.execute("COPY PatientSurveyData FROM 's3://hid-sp18-521/PatientSurveyData.csv' "
                "ACCESS_KEY_ID '" + ACCESS_KEY_ID + "' SECRET_ACCESS_KEY '" + SECRET_ACCESS_KEY + "' "
                "ignoreheader 1 "
                "removequotes "
                "delimiter ',';")

    redshift.commit()

# Clear out all data from the Redshift table PatientSurveyData
def redshift_delete_table_data():
    redshift = psycopg2.connect(dbname= 'i524', host='iu-sp18.c9tuimcojmsj.us-east-1.redshift.amazonaws.com',
                                   port= '5439', user= redshift_user, password= redshift_password)

    cur = redshift.cursor()

    cur.execute("DELETE FROM PatientSurveyData")

    return redshift.commit()

# Query data from the Redshift table PatientSurveyData TODO: Change this to a useful query
def redshift_query_table_data():
    redshift = psycopg2.connect(dbname= 'i524', host='iu-sp18.c9tuimcojmsj.us-east-1.redshift.amazonaws.com',
                                   port= '5439', user= redshift_user, password= redshift_password)

    cur = redshift.cursor()

    cur.execute("SELECT * FROM PatientSurveyData")
    sql = cur.fetchall()
    redshift.commit()

    return sql
