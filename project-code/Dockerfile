FROM ubuntu:16.04
MAINTAINER Scott Steinbruegge <srsteinb@iu.edu>

RUN apt-get update -q && apt-get install -qy \
 build-essential \
    python-dev \
    python-pip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    pandoc \
    wget \
    curl \
    emacs \
    git-core \
    default-jre \
software-properties-common -y

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 2.7.14
RUN pyenv global 2.7.14
RUN python -m ensurepip

RUN git clone https://github.com/cloudmesh-community/hid-sp18-521.git

WORKDIR hid-sp18-521/project-code

RUN mkdir -p cloudmesh-awsdataservices
RUN mkdir -p ~/.cloudmesh
RUN wget https://iu.box.com/shared/static/01za2okav3ly1zl6z545l57wj1gq120m.yml -O ~/.cloudmesh/configuration-awsdataservices.yml
RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
RUN java -jar swagger-codegen-cli.jar generate -i awsdataservices.yml -l python-flask -o cloudmesh-awsdataservices -D supportPython2=true
RUN pip install pymysql boto3 smart_open psycopg2 psycopg2-binary
RUN cp awsdataservices.py cloudmesh-awsdataservices/swagger_server/controllers
RUN cp default_controller.py cloudmesh-awsdataservices/swagger_server/controllers
RUN cd cloudmesh-awsdataservices && pip install -r requirements.txt && python setup.py install

EXPOSE 8080

CMD cd /hid-sp18-521/project-code/cloudmesh-awsdataservices && python -m swagger_server
