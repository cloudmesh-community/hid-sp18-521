SWAGGER-CODEGEN=java -jar swagger-codegen-cli.jar	

service:
	mkdir pds
	$(SWAGGER-CODEGEN) generate -i swagger.yaml -l python-flask -o pds -D supportPython2=true
	cp pdsfunctions.py pds/swagger_server/controllers
	cp config.py pds/swagger_server/controllers
	cp default_controller.py pds/swagger_server/controllers
	cd pds && pip install -r requirements.txt && python setup.py install

clean:
	rm -r pds

start:
	cd pds && python -m swagger_server

stop:
	kill -9 $$(ps -ef | grep "python -m swagger_server" | awk '{print $$2}')

test:
	curl -X GET "http://localhost:8080/cloudmesh/sql/hid-sp18-521/provider" -H "accept: application/json"
	curl -X GET "http://localhost:8080/cloudmesh/sql/hid-sp18-521/provider/1234567890" -H  "accept: application/json"
	curl -X PUT  "http://localhost:8080/cloudmesh/sql/hid-sp18-521/provider" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"npi\": 2145672234, \"provider_type\": \"Individual\", \"first_name\": \"Laura\", \"last_name\": \"Steinbruegge\", \"ssn\": 999887777}"
	curl -X PATCH "http://localhost:8080/cloudmesh/sql/hid-sp18-521/provider/2145672234" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"npi\": 2145672234, \"provider_type\": \"Individual\", \"first_name\": \"Laura\", \"last_name\": \"NameChanged\", \"ssn\": 999887777}"
	curl -X DELETE "http://localhost:8080/cloudmesh/sql/hid-sp18-521/provider/2145672234" -H  "accept: application/json"

	








	








