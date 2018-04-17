import connexion
import six
import awsdataservices

from swagger_server.models.avg_star_rating_per_state import AvgStarRatingPerState  # noqa: E501
from swagger_server.models.data_pipeline_status import DataPipelineStatus  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.patient_survey_data import PatientSurveyData  # noqa: E501
from swagger_server.models.s3_file_names import S3FileNames  # noqa: E501
from swagger_server import util


def copy_cs_vto_s3():  # noqa: E501
    """copy_cs_vto_s3

    Copies the Medicare data set used in CSV format for this project directly from web to an S3 bucket. # noqa: E501


    :rtype: None
    """
    return awsdataservices.medicare_patient_survey_data_csv_to_s3()


def copy_jso_nto_s3():  # noqa: E501
    """copy_jso_nto_s3

    Copies the Medicare data set used in JSON format for this project directly from web to an S3 bucket. # noqa: E501


    :rtype: None
    """
    return awsdataservices.medicare_patient_survey_data_json_to_s3()


def create_athena_table():  # noqa: E501
    """create_athena_table

    Creates the table PatientSurveyData on Athena. # noqa: E501


    :rtype: None
    """
    return awsdataservices.athena_create_table()


def create_dynamo_db_table():  # noqa: E501
    """create_dynamo_db_table

    Creates the table PatientSurveyData from DynamoDB. # noqa: E501


    :rtype: None
    """
    return awsdataservices.dynamodb_create_table()


def delete_athena_table():  # noqa: E501
    """delete_athena_table

    Deletes the table PatientSurveyData on Athena. # noqa: E501


    :rtype: None
    """
    return awsdataservices.athena_drop_table()


def delete_dynamo_db_table():  # noqa: E501
    """delete_dynamo_db_table

    Deletes the table PatientSurveyData from DynamoDB. # noqa: E501


    :rtype: None
    """
    return awsdataservices.dynamodb_delete_table()


def delete_redshift_table():  # noqa: E501
    """delete_redshift_table

    Deletes all data from the table PatientSurveyData on Redshift. # noqa: E501


    :rtype: None
    """
    return awsdataservices.redshift_delete_table_data()


def get_patient_survey_data_athena(city):  # noqa: E501
    """get_patient_survey_data_athena

    Queries the table PatientSurveyData for data matching the city parameter on Athena and places the query output in CSV file on S3. # noqa: E501

    :param city: Show all patient survey results for hospitals located in the city provided.
    :type city: str

    :rtype: None
    """
    return awsdataservices.athena_query_table(city)


def get_patient_survey_data_dynamo_db():  # noqa: E501
    """get_patient_survey_data_dynamo_db

    Runs a scan on the PatientSurveyData data stored in DynamoDB to return all results for hospitals located in the state of MO. # noqa: E501


    :rtype: List[PatientSurveyData]
    """
    return awsdataservices.dynamodb_query_data()


def get_patient_survey_data_rds(starRating):  # noqa: E501
    """get_patient_survey_data_rds

    Runs a select query on the PatientSurveyData data stored in a mySQL RDS instance that we imported into from the Data Pipeline job. # noqa: E501

    :param starRating: Star rating for the patient survey data we&#39;d like to see
    :type starRating: str

    :rtype: List[PatientSurveyData]
    """
    return awsdataservices.query_mysql_data(starRating)


def get_patient_survey_data_redshift():  # noqa: E501
    """get_patient_survey_data_redshift

    Runs a query on the PatientSurveyData data stored in Redshift to return the average star rating for hospitals in each state. # noqa: E501


    :rtype: List[AvgStarRatingPerState]
    """
    return awsdataservices.redshift_query_table_data()


def get_s3_file_names():  # noqa: E501
    """get_s3_file_names

    Returns the list of all files stored in the S3 bucket hid-sp18-521. # noqa: E501


    :rtype: List[S3FileNames]
    """
    return awsdataservices.s3_bucket_allfiles()


def get_status_insert_patient_survey_data_s3to_rds():  # noqa: E501
    """get_status_insert_patient_survey_data_s3to_rds

    Returns the list of all files stored in the S3 bucket hid-sp18-521. # noqa: E501


    :rtype: List[DataPipelineStatus]
    """
    return awsdataservices.data_pipeline_s3_to_rds_status()


def insert_patient_survey_data_s3to_rds():  # noqa: E501
    """insert_patient_survey_data_s3to_rds

    Starts the AWS Data Pipeline job to import the raw Medicare data file from S3 into a mySQL database running on Amazon RDS. # noqa: E501


    :rtype: None
    """
    return awsdataservices.data_pipeline_s3_to_rds()


def load_dynamo_db_table():  # noqa: E501
    """load_dynamo_db_table

    Loads the table PatientSurveyData from a JSON file stored in S3. # noqa: E501


    :rtype: None
    """
    return awsdataservices.dynamodb_insert_json_file()


def load_redshift_table():  # noqa: E501
    """load_redshift_table

    Loads the table PatientSurveyData from a CSV file stored in S3 into a Redshift table. # noqa: E501


    :rtype: None
    """
    return awsdataservices.redshift_load_table_from_s3()
