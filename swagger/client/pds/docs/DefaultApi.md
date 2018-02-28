# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8080/PDS*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider**](DefaultApi.md#create_provider) | **PUT** /provider | 
[**delete_provider**](DefaultApi.md#delete_provider) | **DELETE** /provider/{npi} | 
[**get_provider**](DefaultApi.md#get_provider) | **GET** /provider/{npi} | 
[**get_providers**](DefaultApi.md#get_providers) | **GET** /provider | 
[**update_provider**](DefaultApi.md#update_provider) | **PATCH** /provider/{npi} | 


# **create_provider**
> create_provider(provider=provider)



User can insert a new provider record.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**Provider**](Provider.md)| Creates a new medical provider record. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provider**
> delete_provider(npi)



Delete a single provider based on NPI supplied.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
npi = 56 # int | NPI of provider to delete

try:
    api_instance.delete_provider(npi)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npi** | **int**| NPI of provider to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provider**
> list[Provider] get_provider(npi)



Returns medical provider of the speicifed provider NPI

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
npi = 56 # int | Provider type of providers to return

try:
    api_response = api_instance.get_provider(npi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npi** | **int**| Provider type of providers to return | 

### Return type

[**list[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> list[Provider] get_providers()



Returns all medical providers in the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_providers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_providers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider**
> list[Provider] update_provider(npi, provider=provider)



Update a providers information based on NPI supplied

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
npi = 56 # int | NPI of provider to update
provider = swagger_client.Provider() # Provider | Data for update (optional)

try:
    api_response = api_instance.update_provider(npi, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npi** | **int**| NPI of provider to update | 
 **provider** | [**Provider**](Provider.md)| Data for update | [optional] 

### Return type

[**list[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

