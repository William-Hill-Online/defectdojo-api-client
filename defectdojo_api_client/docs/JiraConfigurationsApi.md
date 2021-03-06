# defectdojo_api_client.JiraConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_configurations_create**](JiraConfigurationsApi.md#jira_configurations_create) | **POST** /jira_configurations/ | 
[**jira_configurations_delete**](JiraConfigurationsApi.md#jira_configurations_delete) | **DELETE** /jira_configurations/{id}/ | 
[**jira_configurations_list**](JiraConfigurationsApi.md#jira_configurations_list) | **GET** /jira_configurations/ | 
[**jira_configurations_partial_update**](JiraConfigurationsApi.md#jira_configurations_partial_update) | **PATCH** /jira_configurations/{id}/ | 
[**jira_configurations_read**](JiraConfigurationsApi.md#jira_configurations_read) | **GET** /jira_configurations/{id}/ | 
[**jira_configurations_update**](JiraConfigurationsApi.md#jira_configurations_update) | **PUT** /jira_configurations/{id}/ | 


# **jira_configurations_create**
> JIRAConf jira_configurations_create(data)



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
    api_instance = defectdojo_api_client.JiraConfigurationsApi(api_client)
    data = defectdojo_api_client.JIRAConf() # JIRAConf | 

    try:
        api_response = api_instance.jira_configurations_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraConfigurationsApi->jira_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

# **jira_configurations_delete**
> jira_configurations_delete(id)



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
    api_instance = defectdojo_api_client.JiraConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ conf.

    try:
        api_instance.jira_configurations_delete(id)
    except ApiException as e:
        print("Exception when calling JiraConfigurationsApi->jira_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 

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

# **jira_configurations_list**
> InlineResponse2005 jira_configurations_list(id=id, url=url, limit=limit, offset=offset)



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
    api_instance = defectdojo_api_client.JiraConfigurationsApi(api_client)
    id = 3.4 # float |  (optional)
url = 'url_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.jira_configurations_list(id=id, url=url, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraConfigurationsApi->jira_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **url** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **jira_configurations_partial_update**
> JIRAConf jira_configurations_partial_update(id, data)



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
    api_instance = defectdojo_api_client.JiraConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ conf.
data = defectdojo_api_client.JIRAConf() # JIRAConf | 

    try:
        api_response = api_instance.jira_configurations_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraConfigurationsApi->jira_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

# **jira_configurations_read**
> JIRAConf jira_configurations_read(id)



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
    api_instance = defectdojo_api_client.JiraConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ conf.

    try:
        api_response = api_instance.jira_configurations_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraConfigurationsApi->jira_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

# **jira_configurations_update**
> JIRAConf jira_configurations_update(id, data)



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
    api_instance = defectdojo_api_client.JiraConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_ conf.
data = defectdojo_api_client.JIRAConf() # JIRAConf | 

    try:
        api_response = api_instance.jira_configurations_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraConfigurationsApi->jira_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

