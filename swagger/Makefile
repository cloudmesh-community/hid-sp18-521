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







	








