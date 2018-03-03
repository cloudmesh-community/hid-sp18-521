# swagger-client
An API that interacts with a SQL database backend of medical provider data system.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.DefaultApi()
provider = swagger_client.Provider() # Provider | Creates a new medical provider record. (optional)

try:
    api_instance.create_provider(provider=provider)
except ApiException as e:
    print("Exception when calling DefaultApi->create_provider: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/PDS*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**create_provider**](docs/DefaultApi.md#create_provider) | **PUT** /provider | 
*DefaultApi* | [**delete_provider**](docs/DefaultApi.md#delete_provider) | **DELETE** /provider/{npi} | 
*DefaultApi* | [**get_provider**](docs/DefaultApi.md#get_provider) | **GET** /provider/{npi} | 
*DefaultApi* | [**get_providers**](docs/DefaultApi.md#get_providers) | **GET** /provider | 
*DefaultApi* | [**update_provider**](docs/DefaultApi.md#update_provider) | **PATCH** /provider/{npi} | 


## Documentation For Models

 - [InlineResponse400](docs/InlineResponse400.md)
 - [Provider](docs/Provider.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


