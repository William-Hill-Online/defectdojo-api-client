# defectdojo_openapi.JiraProductConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_product_configurations_create**](JiraProductConfigurationsApi.md#jira_product_configurations_create) | **POST** /jira_product_configurations/ | 
[**jira_product_configurations_delete**](JiraProductConfigurationsApi.md#jira_product_configurations_delete) | **DELETE** /jira_product_configurations/{id}/ | 
[**jira_product_configurations_list**](JiraProductConfigurationsApi.md#jira_product_configurations_list) | **GET** /jira_product_configurations/ | 
[**jira_product_configurations_partial_update**](JiraProductConfigurationsApi.md#jira_product_configurations_partial_update) | **PATCH** /jira_product_configurations/{id}/ | 
[**jira_product_configurations_read**](JiraProductConfigurationsApi.md#jira_product_configurations_read) | **GET** /jira_product_configurations/{id}/ | 
[**jira_product_configurations_update**](JiraProductConfigurationsApi.md#jira_product_configurations_update) | **PUT** /jira_product_configurations/{id}/ | 


# **jira_product_configurations_create**
> JIRA jira_product_configurations_create(data)



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
    api_instance = defectdojo_openapi.JiraProductConfigurationsApi(api_client)
    data = defectdojo_openapi.JIRA() # JIRA | 

    try:
        api_response = api_instance.jira_product_configurations_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JIRA**](JIRA.md)|  | 

### Return type

[**JIRA**](JIRA.md)

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

# **jira_product_configurations_delete**
> jira_product_configurations_delete(id)



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
    api_instance = defectdojo_openapi.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_p key.

    try:
        api_instance.jira_product_configurations_delete(id)
    except ApiException as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 

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

# **jira_product_configurations_list**
> InlineResponse2007 jira_product_configurations_list(id=id, conf=conf, product=product, component=component, project_key=project_key, push_all_issues=push_all_issues, enable_engagement_epic_mapping=enable_engagement_epic_mapping, push_notes=push_notes, limit=limit, offset=offset)



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
    api_instance = defectdojo_openapi.JiraProductConfigurationsApi(api_client)
    id = 3.4 # float |  (optional)
conf = 'conf_example' # str |  (optional)
product = 'product_example' # str |  (optional)
component = 'component_example' # str |  (optional)
project_key = 'project_key_example' # str |  (optional)
push_all_issues = 'push_all_issues_example' # str |  (optional)
enable_engagement_epic_mapping = 'enable_engagement_epic_mapping_example' # str |  (optional)
push_notes = 'push_notes_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.jira_product_configurations_list(id=id, conf=conf, product=product, component=component, project_key=project_key, push_all_issues=push_all_issues, enable_engagement_epic_mapping=enable_engagement_epic_mapping, push_notes=push_notes, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **conf** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **component** | **str**|  | [optional] 
 **project_key** | **str**|  | [optional] 
 **push_all_issues** | **str**|  | [optional] 
 **enable_engagement_epic_mapping** | **str**|  | [optional] 
 **push_notes** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **jira_product_configurations_partial_update**
> JIRA jira_product_configurations_partial_update(id, data)



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
    api_instance = defectdojo_openapi.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_p key.
data = defectdojo_openapi.JIRA() # JIRA | 

    try:
        api_response = api_instance.jira_product_configurations_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 
 **data** | [**JIRA**](JIRA.md)|  | 

### Return type

[**JIRA**](JIRA.md)

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

# **jira_product_configurations_read**
> JIRA jira_product_configurations_read(id)



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
    api_instance = defectdojo_openapi.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_p key.

    try:
        api_response = api_instance.jira_product_configurations_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 

### Return type

[**JIRA**](JIRA.md)

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

# **jira_product_configurations_update**
> JIRA jira_product_configurations_update(id, data)



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
    api_instance = defectdojo_openapi.JiraProductConfigurationsApi(api_client)
    id = 56 # int | A unique integer value identifying this jir a_p key.
data = defectdojo_openapi.JIRA() # JIRA | 

    try:
        api_response = api_instance.jira_product_configurations_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 
 **data** | [**JIRA**](JIRA.md)|  | 

### Return type

[**JIRA**](JIRA.md)

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

