FROM ubuntu:16.04
MAINTAINER Scott Steinbruegge <srsteinb@iu.edu>

RUN apt-get update
RUN apt-get install default-jre wget curl git-core python-pip -y

RUN git clone https://github.com/cloudmesh-community/hid-sp18-521.git

WORKDIR hid-sp18-521/swagger

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
RUN java -jar swagger-codegen-cli.jar generate -i swagger.yaml -l python-flask -o pds -D supportPython2=true
RUN cp pdsfunctions.py pds/swagger_server/controllers
RUN cp config.py pds/swagger_server/controllers
RUN cp default_controller.py pds/swagger_server/controllers
RUN cd pds && pip install -r requirements.txt && python setup.py install

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["-m", "swagger_server"]









