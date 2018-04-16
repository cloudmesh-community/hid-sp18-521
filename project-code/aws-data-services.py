import boto3, smart_open, pprint, pymysql, urllib, json, decimal, psycopg2, yaml, os
from boto3.dynamodb.conditions import Key, Attr

# Add code here to copy config file if it doesn't exist yet
# AND Add steps to the Makefile setup to copy my config file to this path

if os.path.exists(os.path.expanduser("~/.cloudmesh/configuration-aws-data-services.yml")):
    with open(os.path.expanduser("~/.cloudmesh/configuration-aws-data-services.yml"), 'r') as ymlfile:
        config = yaml.load(ymlfile)

mysql_user = config['cloudmesh']['aws-data-services']['mysql']['user']['name']
mysql_password = config['cloudmesh']['aws-data-services']['mysql']['user']['password']
redshift_user = config['cloudmesh']['aws-data-services']['redshift']['user']['name']
redshift_password = config['cloudmesh']['aws-data-services']['redshift']['user']['password']
k1 = config['cloudmesh']['aws-data-services']['misc']['k1']
k2 = config['cloudmesh']['aws-data-services']['misc']['k2']

# S3 bucket name = hid-sp18-521

# https://data.medicare.gov/Hospital-Compare/Patient-survey-HCAHPS-Hospital/dgck-syfz

# Pulls Medicare hospital survey data set in CSV format directly from their web site into an S3 bucket
def medicare_patient_survey_data_csv_to_s3():
    with smart_open.smart_open('s3://' + k1 + ':' + k2 +'@hid-sp18-521/PatientSurveyData.csv', 'wb') as fout:
        for line in smart_open.smart_open('https://data.medicare.gov/resource/rmgi-5fhi.csv'):
            response = fout.write(line + '\n')
            return response

# Pulls Medicare patient survey data set in JSON format directly from their web site into an S3 bucket
def medicare_patient_survey_data_json_to_s3():
    with smart_open.smart_open('s3://' + k1 + ':' + k2 +'@hid-sp18-521/PatientSurveyData.json', 'wb') as fout:
        for line in smart_open.smart_open('https://data.medicare.gov/resource/rmgi-5fhi.json'):
            response = fout.write(line + '\n')
            return response

# Pulls a list of all of the files that exist in the bucket this application uses
def s3_bucket_allfiles():
    file_names = []

    s3 = boto3.resource('s3', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)
    bucket = s3.Bucket('hid-sp18-521')

    for object in bucket.objects.all():
        file_names.append(object.key)

    return file_names

# Import S3 File into RDS using AWS Data Pipeline (show how it was created and how it can be called from here)
def data_pipeline_s3_to_rds():
    pipeline = boto3.client('datapipeline', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    response = pipeline.activate_pipeline(pipelineId='df-09855991V8LTRRRNJOQW')

    return response

# Return the runtime status of the S3 to RDS data pipelines
def data_pipeline_s3_to_rds_status():
    pipeline = boto3.client('datapipeline', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    pipeline_status = pipeline.describe_pipelines(pipelineIds=['df-09855991V8LTRRRNJOQW'])

    fields = pipeline_status['pipelineDescriptionList'][0]['fields']

    for field in fields:
        if field['key'] == '@pipelineState':
            return field['stringValue']

# Query the table that contains the data we imported into MySQL on RDS from S3
def query_mysql_data(starRating):
    connection = pymysql.connect(host='iu-sp18.cgnrvgmckfic.us-east-1.rds.amazonaws.com',
                                 user=mysql_user,
                                 password=mysql_password,
                                 db='I524',
                                 charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    sql = "SELECT * FROM PatientSurveyData WHERE patient_survey_star_rating = %s"
    cursor.execute(sql, (starRating))
    result = cursor.fetchall()
    return result

# Delete the DynamoDB table PatientSurveyData
def dynamodb_delete_table():
    dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    response = dynamodb.delete_table(TableName='PatientSurveyData')

    return response

# Create the DynamoDB table PatientSurveyData
def dynamodb_create_table():
    dynamodb = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)
    response = dynamodb.create_table(TableName='PatientSurveyData',
                                  KeySchema=[{'AttributeName': 'provider_id', 'KeyType': 'HASH'}, ],
                                  AttributeDefinitions=[{'AttributeName': 'provider_id', 'AttributeType': 'S'}],
                                  ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5},
                                  )
    return response

#Import JSON file from web and into DynamoDB table (wait a minute until the table is created)
def dynamodb_insert_json_file():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    table = dynamodb.Table('PatientSurveyData')

    url = "https://data.medicare.gov/resource/rmgi-5fhi.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read(), parse_float=decimal.Decimal)

    for row in data:
        response = table.put_item(Item=row)

    return response

# Query the data set we just inserted into DymamoDB (Get all hospitals from the survey located in Missouri)
def dynamodb_query_data():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

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
                "ACCESS_KEY_ID '" + k1 + "' SECRET_ACCESS_KEY '" + k2 + "' "
                "ignoreheader 1 "
                "removequotes "
                "delimiter ',';")

    return redshift.commit()

# Clear out all data from the Redshift table PatientSurveyData
def redshift_delete_table_data():
    redshift = psycopg2.connect(dbname= 'i524', host='iu-sp18.c9tuimcojmsj.us-east-1.redshift.amazonaws.com',
                                   port= '5439', user= redshift_user, password= redshift_password)

    cur = redshift.cursor()

    cur.execute("DELETE FROM PatientSurveyData")

    return redshift.commit()

# Query data from the Redshift table PatientSurveyData
def redshift_query_table_data():
    redshift = psycopg2.connect(dbname= 'i524', host='iu-sp18.c9tuimcojmsj.us-east-1.redshift.amazonaws.com',
                                   port= '5439', user= redshift_user, password= redshift_password)

    cur = redshift.cursor()

    cur.execute("select location_state, avg(patient_survey_star_rating) from PatientSurveyData "
                "where patient_survey_star_rating in (1,2,3,4,5) group by location_state order by location_state")

    sql = cur.fetchall()
    redshift.commit()

    return sql

def athena_create_database():
    athena = boto3.client('athena', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    response = athena.start_query_execution(
            QueryString='CREATE DATABASE IF NOT EXISTS i524',
            QueryExecutionContext={'Database': 'default'}, ResultConfiguration={'OutputLocation': 's3://hid-sp18-521/athena-output'})

    return response

def athena_create_table():
    athena = boto3.client('athena', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    with smart_open.smart_open('s3://' + k1 + ':' + k2 +'@hid-sp18-521/athena-input/PatientSurveyData.csv', 'wb') as fout:
        for line in smart_open.smart_open('https://data.medicare.gov/resource/rmgi-5fhi.csv'):
            response = fout.write(line + '\n')

    response = athena.start_query_execution(
        QueryString="""CREATE EXTERNAL TABLE IF NOT EXISTS i524.PatientSurveyData (
                    computed_region_csmy_5jwy string,	
                    computed_region_f3tr_pr43 string,
                    computed_region_nwen_78xc string,
                    address string,
                    city string,
                    county_name string,
                    hcahps_answer_description string,
                    hcahps_answer_percent string,
                    hcahps_answer_percent_footnote string,
                    hcahps_linear_mean_value string,
                    hcahps_measure_id string,
                    hcahps_question string,
                    hospital_name string,
                    location string,
                    location_address string,
                    location_city string,
                    location_state string,
                    location_zip string,
                    measure_end_date string,
                    measure_start_date string,
                    number_of_completed_surveys string,
                    number_of_completed_surveys_footnote string,
                    patient_survey_star_rating string,
                    patient_survey_star_rating_footnote	string,
                    phone_number string,
                    phone_number_type string,
                    provider_id	string,
                    state string,
                    survey_response_rate_percent string,
                    survey_response_rate_percent_footnote string,
                    zip_code string
         )
         ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
         WITH SERDEPROPERTIES (
           'separatorChar' = ',',
           'quoteChar' = '\"'
         )
         STORED AS TEXTFILE 
         LOCATION 's3://hid-sp18-521/athena-input'
         TBLPROPERTIES ("skip.header.line.count"="1");""",
        QueryExecutionContext={'Database': 'i524'}, ResultConfiguration={'OutputLocation': 's3://hid-sp18-521'})

    return response

def athena_drop_table():
    athena = boto3.client('athena', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    response = athena.start_query_execution(
        QueryString="DROP TABLE IF EXISTS PatientSurveyData",
        QueryExecutionContext={'Database': 'i524'}, ResultConfiguration={'OutputLocation': 's3://hid-sp18-521'})

    return response

def athena_query_table(city):
    athena = boto3.client('athena', region_name='us-east-1', aws_access_key_id=k1, aws_secret_access_key=k2)

    query = 'SELECT * FROM patientsurveydata WHERE city = \'%s\'' % (city)
    print query

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': 'i524'}, ResultConfiguration={'OutputLocation': 's3://hid-sp18-521'})

    return response
