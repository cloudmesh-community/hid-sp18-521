# Swagger REST API Assignment - SQL Database Interactions
This folder contains the files necessary to create and deploy a server side REST API that showcases how to use CRUD operations against a SQL database backend that resides on a MySQL Amazon RDS instance. It shows how a REST API can be used to select, insert, update and delete data from a medical provider database using various HTTP methods such as GET, PUT, PATCH and DELETE. I chose this for my assignment because I have limited software development knowledge and I was always curious how a front end application makes various types of calls to a SQL database backend. 

### Installation and Usage (steps tested and working for Ubuntu 16.04)
1. Open a terminal window and change directory to the folder you want to install the service in.
2. Run the commands below to clone my Git repository to your machine and the navigate to the swagger folder: 
    ```sh
    git clone https://github.com/cloudmesh-community/hid-sp18-521.git
    cd hid-sp18-521/swagger
    ```
3. Additional steps can then be performed by excuting the Makefile using the usage parameters below:
    -  Installing the sevice and dependencies
        ```sh
        make service
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
    -  Test the service using GET, PUT, PATCH and DELETE curl calls:
        ```sh
        make test
        ```
    -  Create a Docker image and container named cloudmesh-sql using Dockerfile:
        ```sh
        make container
        ```
    -  Run the Docker container named cloudmesh-sql:
        ```sh
        make container_start
        ```
