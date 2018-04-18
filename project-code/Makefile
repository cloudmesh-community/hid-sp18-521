install:
	mkdir cloudmesh-awsdataservices
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i awsdataservices.yml -l python-flask -o cloudmesh-awsdataservices -D supportPython2=true
	pip install pymysql boto3 smart_open psycopg2 
	cp awsdataservices.py cloudmesh-awsdataservices/swagger_server/controllers
	cp default_controller.py cloudmesh-awsdataservices/swagger_server/controllers
	cp etc/configuration-awsdataservices.yml ~/.cloudmesh
	cd cloudmesh-awsdataservices && pip install -r requirements.txt && python setup.py install

clean:
	rm -r cloudmesh-awsdataservices
	rm swagger-codegen-cli.jar

start:
	cd cloudmesh-awsdataservices && python -m swagger_server

stop:
	kill -9 $$(ps -ef | grep "python -m swagger_server" | awk '{print $$2}')

test-copy-files-to-s3:
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/csv-to-s3" -H "accept: application/json"	
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/json-to-s3" -H "accept: application/json"	

test-s3-files:
	curl -X GET "http://localhost:8080/cloudmesh/aws-data-services/s3-files" -H "accept: application/json"

test-data-pipeline-start:
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/data-pipeline-s3-to-rds" -H "accept: application/json"	

test-data-pipeline-status:
	curl -X GET "http://localhost:8080/cloudmesh/aws-data-services/data-pipeline-s3-to-rds-status" -H "accept: application/json"	

test-rds:
	curl -X GET "http://localhost:8080/cloudmesh/aws-data-services/rds-mysql-query/5" -H "accept: application/json"	

test-dynamodb:
	curl -X DELETE "http://localhost:8080/cloudmesh/aws-data-services/dynamo-db-delete-table" -H "accept: application/json"	
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/dynamo-db-create-table" -H "accept: application/json"	
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/dynamo-db-insert-json" -H "accept: application/json"	
	curl -X GET "http://localhost:8080/cloudmesh/aws-data-services/dynamo-query-table" -H "accept: application/json"	

test-redshift:
	curl -X DELETE "http://localhost:8080/cloudmesh/aws-data-services/redshift-delete-table" -H "accept: application/json"	
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/redshift-insert-csv-from-s3" -H "accept: application/json"	
	curl -X GET "http://localhost:8080/cloudmesh/aws-data-services/redshift-query-table" -H "accept: application/json"	

test-athena:
	curl -X DELETE "http://localhost:8080/cloudmesh/aws-data-services/athena-delete-table" -H "accept: application/json"
	curl -X PUT "http://localhost:8080/cloudmesh/aws-data-services/athena-create-table" -H "accept: application/json"		
	curl -X GET "http://localhost:8080/cloudmesh/aws-data-services/athena-query-table/TAOS" -H "accept: application/json"	

container:
	docker build -t cloudmesh-awsdataservices .
	docker create cloudmesh-awsdataservices

container_start:
	docker run cloudmesh-awsdataservices 



