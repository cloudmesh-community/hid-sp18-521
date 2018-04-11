service:
	mkdir pds
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i sql-aws.yml -l python-flask -o pds -D supportPython2=true
	pip install pymysql
	cp pdsfunctions.py pds/swagger_server/controllers
	cp config.py pds/swagger_server/controllers
	cp default_controller.py pds/swagger_server/controllers
	cd pds && pip install -r requirements.txt && python setup.py install

clean:
	rm -r pds
	rm swagger-codegen-cli.jar

start:
	cd pds && python -m swagger_server

stop:
	kill -9 $$(ps -ef | grep "python -m swagger_server" | awk '{print $$2}')

test:
	curl -X GET "http://localhost:8080/cloudmesh/sql/provider" -H "accept: application/json"
	curl -X GET "http://localhost:8080/cloudmesh/sql/provider/1234567890" -H  "accept: application/json"
	curl -X PUT  "http://localhost:8080/cloudmesh/sql/provider" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"npi\": 2145672234, \"provider_type\": \"Individual\", \"first_name\": \"Laura\", \"last_name\": \"Steinbruegge\", \"ssn\": 999887777}"
	curl -X PATCH "http://localhost:8080/cloudmesh/sql/provider/2145672234" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"npi\": 2145672234, \"provider_type\": \"Individual\", \"first_name\": \"Laura\", \"last_name\": \"NameChanged\", \"ssn\": 999887777}"
	curl -X DELETE "http://localhost:8080/cloudmesh/sql/provider/2145672234" -H  "accept: application/json"

container:
	docker build -t cloudmesh-sql .
	docker create cloudmesh-sql

container_start:
	docker start cloudmesh-sql 

	
	








	








