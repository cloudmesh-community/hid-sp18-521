Swagger assignment to show how a REST API interacts with a SQL database on Amazon RDS using various HTTP methods.

Sample curl calls for used for testing:

- curl -X GET "http://localhost:8080/PDS/provider" -H "accept: application/json"	

- curl -X GET "http://localhost:8080/PDS/provider/1234567890" -H  "accept: application/json"

- curl -X POST "http://localhost:8080/PDS/provider" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"npi\": 2145672234, \"provider_type\": \"Individual\", \"first_name\": \"Laura\", \"last_name\": \"Steinbruegge\", \"ssn\": 999887777}"

- curl -X DELETE "http://localhost:8080/PDS/provider/1234567899" -H  "accept: application/json"

Key Files:

swagger.yaml - contains the Swaagger specification for a medical provider API to perform CRUD operations against a MySQL database  sitting on Amazon RDS.
