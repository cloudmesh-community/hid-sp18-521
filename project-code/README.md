# Final Project Code - Interacting With Data Services on AWS
This folder contains all of the files and code necessary to implement and test our project that aims to showcase how to interact with AWS data related services from Swagger REST API's using the Python SDK for AWS named Boto. While some of the project work was done in AWS Management Console since we did not want to expose AWS server creation over an API due to cost concerns, the majority of the interactions are done within Boto. In order to show how to programatically interact with these AWS services, we will use a Medicare data set that contains patient survey results for hospitals throughout the country. This data set will be used in both JSON and CSV format and will be used in six differnt AWS services: S3, Data Pipeline, RDS, DynamoDB, Redshift and Athena. 

### Installation and Usage (steps tested and working for Ubuntu 16.04 and Python 2.7)
1. Open a terminal window and change directory to the folder you want to install the service in.
2. Run the commands below to clone my Git repository to your machine and the navigate to the project-code folder: 
    ```sh
    git clone https://github.com/cloudmesh-community/hid-sp18-521.git
    cd hid-sp18-521/project-code
    ```
3. Additional steps can then be performed by excuting the Makefile using the usage parameters below:
    -  Installing the Swagger service and code dependencies
        ```sh
        make install
        ```
    -  Remove service and cleanup files
        ```sh
        make clean
        ```
    -  Start the service
        ```sh
        make start
        ```
    -  Stop the service
        ```sh
        make stop
        ```
    -  Copy the Medicare data file in CSV and JSON format from the Medicare website to an S3 bucket:
        ```sh
        make test-copy-files-to-s3
        ```
    -  Lists all of the files stored in the S3 bucket related to this project:
        ```sh
        make test-s3-files
        ```
    -  Starts the Data Pipeline job to import the Medicare CSV file into a MySQL database on Amazon RDS (this might take about 5 minutes to complete):
        ```sh
        make test-data-pipeline-start
        ```
    -  Create a Docker image and container named cloudmesh-awsdataservices using Dockerfile:
        ```sh
        make container
        ```
    -  Run the Docker container named cloudmesh-awsdataservices:
        ```sh
        make container-start
        ```
