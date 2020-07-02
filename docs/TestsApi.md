# defectdojo_openapi.TestsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tests_accept_risks**](TestsApi.md#tests_accept_risks) | **POST** /tests/{id}/accept_risks/ | 
[**tests_create**](TestsApi.md#tests_create) | **POST** /tests/ | 
[**tests_delete**](TestsApi.md#tests_delete) | **DELETE** /tests/{id}/ | 
[**tests_generate_report**](TestsApi.md#tests_generate_report) | **POST** /tests/{id}/generate_report/ | 
[**tests_list**](TestsApi.md#tests_list) | **GET** /tests/ | 
[**tests_partial_update**](TestsApi.md#tests_partial_update) | **PATCH** /tests/{id}/ | 
[**tests_read**](TestsApi.md#tests_read) | **GET** /tests/{id}/ | 
[**tests_update**](TestsApi.md#tests_update) | **PUT** /tests/{id}/ | 


# **tests_accept_risks**
> RiskAcceptance tests_accept_risks(id, data)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = [defectdojo_openapi.AcceptedRisk()] # list[AcceptedRisk] | 

    try:
        api_response = api_instance.tests_accept_risks(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_accept_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**list[AcceptedRisk]**](AcceptedRisk.md)|  | 

### Return type

[**RiskAcceptance**](RiskAcceptance.md)

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

# **tests_create**
> TestCreate tests_create(data)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    data = defectdojo_openapi.TestCreate() # TestCreate | 

    try:
        api_response = api_instance.tests_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TestCreate**](TestCreate.md)|  | 

### Return type

[**TestCreate**](TestCreate.md)

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

# **tests_delete**
> tests_delete(id)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_instance.tests_delete(id)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

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

# **tests_generate_report**
> ReportGenerate tests_generate_report(id, data)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = defectdojo_openapi.ReportGenerateOption() # ReportGenerateOption | 

    try:
        api_response = api_instance.tests_generate_report(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**ReportGenerateOption**](ReportGenerateOption.md)|  | 

### Return type

[**ReportGenerate**](ReportGenerate.md)

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

# **tests_list**
> InlineResponse20018 tests_list(id=id, title=title, test_type=test_type, target_start=target_start, target_end=target_end, notes=notes, percent_complete=percent_complete, actual_time=actual_time, engagement=engagement, limit=limit, offset=offset)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 3.4 # float |  (optional)
title = 'title_example' # str |  (optional)
test_type = 'test_type_example' # str |  (optional)
target_start = 'target_start_example' # str |  (optional)
target_end = 'target_end_example' # str |  (optional)
notes = 'notes_example' # str |  (optional)
percent_complete = 3.4 # float |  (optional)
actual_time = 'actual_time_example' # str |  (optional)
engagement = 'engagement_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.tests_list(id=id, title=title, test_type=test_type, target_start=target_start, target_end=target_end, notes=notes, percent_complete=percent_complete, actual_time=actual_time, engagement=engagement, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **title** | **str**|  | [optional] 
 **test_type** | **str**|  | [optional] 
 **target_start** | **str**|  | [optional] 
 **target_end** | **str**|  | [optional] 
 **notes** | **str**|  | [optional] 
 **percent_complete** | **float**|  | [optional] 
 **actual_time** | **str**|  | [optional] 
 **engagement** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

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

# **tests_partial_update**
> Test tests_partial_update(id, data)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = defectdojo_openapi.Test() # Test | 

    try:
        api_response = api_instance.tests_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**Test**](Test.md)|  | 

### Return type

[**Test**](Test.md)

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

# **tests_read**
> Test tests_read(id)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.

    try:
        api_response = api_instance.tests_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 

### Return type

[**Test**](Test.md)

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

# **tests_update**
> Test tests_update(id, data)



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
    api_instance = defectdojo_openapi.TestsApi(api_client)
    id = 56 # int | A unique integer value identifying this test.
data = defectdojo_openapi.Test() # Test | 

    try:
        api_response = api_instance.tests_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TestsApi->tests_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test. | 
 **data** | [**Test**](Test.md)|  | 

### Return type

[**Test**](Test.md)

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

