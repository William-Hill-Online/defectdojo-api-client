# defectdojo_api_client.SystemSettingsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_settings_list**](SystemSettingsApi.md#system_settings_list) | **GET** /system_settings/ | 
[**system_settings_partial_update**](SystemSettingsApi.md#system_settings_partial_update) | **PATCH** /system_settings/{id}/ | 
[**system_settings_update**](SystemSettingsApi.md#system_settings_update) | **PUT** /system_settings/{id}/ | 


# **system_settings_list**
> InlineResponse20016 system_settings_list(limit=limit, offset=offset)



Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import defectdojo_api_client
from defectdojo_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_client.SystemSettingsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.system_settings_list(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemSettingsApi->system_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_partial_update**
> SystemSettings system_settings_partial_update(id, data)



Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import defectdojo_api_client
from defectdojo_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_client.SystemSettingsApi(api_client)
    id = 56 # int | A unique integer value identifying this system_ settings.
data = defectdojo_api_client.SystemSettings() # SystemSettings | 

    try:
        api_response = api_instance.system_settings_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemSettingsApi->system_settings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this system_ settings. | 
 **data** | [**SystemSettings**](SystemSettings.md)|  | 

### Return type

[**SystemSettings**](SystemSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_settings_update**
> SystemSettings system_settings_update(id, data)



Basic control over System Settings. Use 'id' 1 for PUT, PATCH operations

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import defectdojo_api_client
from defectdojo_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_client.SystemSettingsApi(api_client)
    id = 56 # int | A unique integer value identifying this system_ settings.
data = defectdojo_api_client.SystemSettings() # SystemSettings | 

    try:
        api_response = api_instance.system_settings_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SystemSettingsApi->system_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this system_ settings. | 
 **data** | [**SystemSettings**](SystemSettings.md)|  | 

### Return type

[**SystemSettings**](SystemSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

