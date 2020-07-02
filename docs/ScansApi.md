# defectdojo_openapi.ScansApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scans_list**](ScansApi.md#scans_list) | **GET** /scans/ | 
[**scans_read**](ScansApi.md#scans_read) | **GET** /scans/{id}/ | 


# **scans_list**
> InlineResponse20014 scans_list(id=id, date=date, scan_settings=scan_settings, limit=limit, offset=offset)



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import defectdojo_openapi
from defectdojo_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_openapi.Configuration(
    host = "http://localhost:8080/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = defectdojo_openapi.Configuration(
    host = "http://localhost:8080/api/v2",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_openapi.ScansApi(api_client)
    id = 3.4 # float |  (optional)
date = 'date_example' # str |  (optional)
scan_settings = 'scan_settings_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.scans_list(id=id, date=date, scan_settings=scan_settings, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScansApi->scans_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **date** | **str**|  | [optional] 
 **scan_settings** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

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

# **scans_read**
> Scan scans_read(id)



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import defectdojo_openapi
from defectdojo_openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_openapi.Configuration(
    host = "http://localhost:8080/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = defectdojo_openapi.Configuration(
    host = "http://localhost:8080/api/v2",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_openapi.ScansApi(api_client)
    id = 56 # int | A unique integer value identifying this scan.

    try:
        api_response = api_instance.scans_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScansApi->scans_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan. | 

### Return type

[**Scan**](Scan.md)

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

