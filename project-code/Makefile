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

test:


container:
	docker build -t cloudmesh-awsdataservices .
	docker create cloudmesh-awsdataservices

container_start:
	docker run cloudmesh-awsdataservices 



