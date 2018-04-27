# Final Project Code - Interacting With Data Services on AWS
This folder contains all of the files and code necessary to implement and test our project that aims to showcase how to interact with AWS data related services from Swagger REST API's using the Python SDK for AWS named Boto. While some of the project work was done in AWS Management Console since we did not want to expose AWS server creation over an API due to cost concerns, the majority of the interactions are done within Boto. In order to show how to programatically interact with these AWS services, we will use a Medicare data set that contains patient survey results for hospitals throughout the country. This data set will be used in both JSON and CSV format and will be used in six different AWS services: S3, Data Pipeline, RDS, DynamoDB, Redshift and Athena. 

### Installation and Usage (steps tested and working for Ubuntu 16.04 and Python 2.7)
1. Open a terminal window and change directory to the folder you want to install the service in.
2. Run the commands below to clone my Git repository to your machine and the navigate to the project-code folder: 
    ```sh
    git clone https://github.com/cloudmesh-community/hid-sp18-521.git
    cd hid-sp18-521/project-code
    ```
3. Additional steps can then be performed by executing the Makefile using the commands below:
    -  Installing the Swagger service and code dependencies
        ```sh
        make install
        ```
    -  Start the service
        ```sh
        make start
        ```
Once the service has been started you will need to open a new terminal window and change directory to where the Makefile exists          again (cd yourinstallfolder/hid-sp18-521/project-code), then the addtional commands below can be run:
   
    -  Copy the Medicare data file in CSV and JSON format from the Medicare website to an S3 bucket:
        ```sh
        make test-copy-files-to-s3
        ```
    -  Lists all of the files stored in the S3 bucket related to this project:
        ```sh
        make test-s3-files
        ```
    -  Starts the Data Pipeline job to import the Medicare CSV file stored in S3 into a MySQL database on Amazon RDS (this might take about 5 minutes to complete):
        ```sh
        make test-data-pipeline-start
        ```
    -  Checks the status of the Data Pipeline job started by test-data-pipeline-start:
        ```sh
        make test-data-pipeline-status
        ```
    -  Executes a select query on the PatientSurveyData table in the MySQL database on RDS that contains the S3 CSV data imported by the Data Pipeline job. This example query will return all of the hospitals that received a 5 star rating in the survey:
        ```sh
        make test-rds
        ```
    -  Deletes the table PatientSurveyData from DynamoDB:
        ```sh
        make test-dynamodb-delete-table
        ```
    -  Creates the table PatientSurveyData on DynamoDB (wait 3-4 minutes after running the delete command to run this):
        ```sh
        make test-dynamodb-create-table
        ```
    -  Inserts the patient survey data from the JSON file located in S3 the table PatientSurveyData on DynamoDB. Then runs a table scan on the PatientSurveyData table in DynammoDB to return all hospitals located in the state of MO. This can take about 5 to 10 minutes to complete (also wait 3-4 minutes after running the create table command to run this):
        ```sh
        make test-dynamodb-insert-query-table
        ```
    -  Deletes all data from the Redshift table PatientSurveyData, inserts the S3 CSV survey data into the Redshift table PatientSurveyData and then queries the Redshift table PatientSurveyData to return the average hospital rating per state:
        ```sh
        make test-redshift
        ```
    -  Drops, creates and then queries the Athena table PatientSurveyData (Athena query output is saved to the S3 bucket and not returned to the API):
        ```sh
        make test-athena
        ```
    -  Create a Docker image and container named cloudmesh-awsdataservices using Dockerfile:
        ```sh
        make container
        ```
    -  Run the Docker container named cloudmesh-awsdataservices:
        ```sh
        make container-start
        ```
    -  Stop the service
        ```sh
        make stop
        ```
    -  Remove service and cleanup files
        ```sh
        make clean
        ```
