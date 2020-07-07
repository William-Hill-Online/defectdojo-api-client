# defectdojo_api_client.ScanSettingsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan_settings_create**](ScanSettingsApi.md#scan_settings_create) | **POST** /scan_settings/ | 
[**scan_settings_delete**](ScanSettingsApi.md#scan_settings_delete) | **DELETE** /scan_settings/{id}/ | 
[**scan_settings_list**](ScanSettingsApi.md#scan_settings_list) | **GET** /scan_settings/ | 
[**scan_settings_partial_update**](ScanSettingsApi.md#scan_settings_partial_update) | **PATCH** /scan_settings/{id}/ | 
[**scan_settings_read**](ScanSettingsApi.md#scan_settings_read) | **GET** /scan_settings/{id}/ | 
[**scan_settings_update**](ScanSettingsApi.md#scan_settings_update) | **PUT** /scan_settings/{id}/ | 


# **scan_settings_create**
> ScanSettingsCreate scan_settings_create(data)



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
    api_instance = defectdojo_api_client.ScanSettingsApi(api_client)
    data = defectdojo_api_client.ScanSettingsCreate() # ScanSettingsCreate | 

    try:
        api_response = api_instance.scan_settings_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScanSettingsApi->scan_settings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ScanSettingsCreate**](ScanSettingsCreate.md)|  | 

### Return type

[**ScanSettingsCreate**](ScanSettingsCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_delete**
> scan_settings_delete(id)



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
    api_instance = defectdojo_api_client.ScanSettingsApi(api_client)
    id = 56 # int | A unique integer value identifying this scan settings.

    try:
        api_instance.scan_settings_delete(id)
    except ApiException as e:
        print("Exception when calling ScanSettingsApi->scan_settings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_list**
> InlineResponse20013 scan_settings_list(id=id, date=date, user=user, frequency=frequency, product=product, addresses=addresses, limit=limit, offset=offset)



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
    api_instance = defectdojo_api_client.ScanSettingsApi(api_client)
    id = 3.4 # float |  (optional)
date = 'date_example' # str |  (optional)
user = 'user_example' # str |  (optional)
frequency = 'frequency_example' # str |  (optional)
product = 'product_example' # str |  (optional)
addresses = 'addresses_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.scan_settings_list(id=id, date=date, user=user, frequency=frequency, product=product, addresses=addresses, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScanSettingsApi->scan_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **date** | **str**|  | [optional] 
 **user** | **str**|  | [optional] 
 **frequency** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **addresses** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

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

# **scan_settings_partial_update**
> ScanSettings scan_settings_partial_update(id, data)



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
    api_instance = defectdojo_api_client.ScanSettingsApi(api_client)
    id = 56 # int | A unique integer value identifying this scan settings.
data = defectdojo_api_client.ScanSettings() # ScanSettings | 

    try:
        api_response = api_instance.scan_settings_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScanSettingsApi->scan_settings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 
 **data** | [**ScanSettings**](ScanSettings.md)|  | 

### Return type

[**ScanSettings**](ScanSettings.md)

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

# **scan_settings_read**
> ScanSettings scan_settings_read(id)



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
    api_instance = defectdojo_api_client.ScanSettingsApi(api_client)
    id = 56 # int | A unique integer value identifying this scan settings.

    try:
        api_response = api_instance.scan_settings_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScanSettingsApi->scan_settings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 

### Return type

[**ScanSettings**](ScanSettings.md)

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

# **scan_settings_update**
> ScanSettings scan_settings_update(id, data)



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
    api_instance = defectdojo_api_client.ScanSettingsApi(api_client)
    id = 56 # int | A unique integer value identifying this scan settings.
data = defectdojo_api_client.ScanSettings() # ScanSettings | 

    try:
        api_response = api_instance.scan_settings_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScanSettingsApi->scan_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 
 **data** | [**ScanSettings**](ScanSettings.md)|  | 

### Return type

[**ScanSettings**](ScanSettings.md)

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

