import boto3
import smart_open

# AWS credentials stored in ~/.aws/credentials
# S3 bucket name = hid-sp18-521

# Pulls Medicare patient survey data set directly from their web site into an S3 bucket
def copy_medicare_patient_survey_data_csv_to_s3():
    with smart_open.smart_open('s3://hid-sp18-521/PatientSurveyData.csv', 'wb') as fout:
        for line in smart_open.smart_open('https://data.medicare.gov/resource/rmgi-5fhi.csv'):
            fout.write(line + '\n')

# Pulls a list of all of the files that exist in the bucket this application uses
def get_s3_bucket_allfiles():
    file_names = []

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('hid-sp18-521')

    for object in bucket.objects.all():
        file_names.append(object.key)

    return file_names









