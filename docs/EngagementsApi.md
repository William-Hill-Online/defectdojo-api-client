# defectdojo_openapi.EngagementsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**engagements_accept_risks**](EngagementsApi.md#engagements_accept_risks) | **POST** /engagements/{id}/accept_risks/ | 
[**engagements_close**](EngagementsApi.md#engagements_close) | **POST** /engagements/{id}/close/ | 
[**engagements_create**](EngagementsApi.md#engagements_create) | **POST** /engagements/ | 
[**engagements_delete**](EngagementsApi.md#engagements_delete) | **DELETE** /engagements/{id}/ | 
[**engagements_generate_report**](EngagementsApi.md#engagements_generate_report) | **POST** /engagements/{id}/generate_report/ | 
[**engagements_list**](EngagementsApi.md#engagements_list) | **GET** /engagements/ | 
[**engagements_partial_update**](EngagementsApi.md#engagements_partial_update) | **PATCH** /engagements/{id}/ | 
[**engagements_read**](EngagementsApi.md#engagements_read) | **GET** /engagements/{id}/ | 
[**engagements_reopen**](EngagementsApi.md#engagements_reopen) | **POST** /engagements/{id}/reopen/ | 
[**engagements_update**](EngagementsApi.md#engagements_update) | **PUT** /engagements/{id}/ | 


# **engagements_accept_risks**
> RiskAcceptance engagements_accept_risks(id, data)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
data = [defectdojo_openapi.AcceptedRisk()] # list[AcceptedRisk] | 

    try:
        api_response = api_instance.engagements_accept_risks(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_accept_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
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

# **engagements_close**
> engagements_close(id)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_instance.engagements_close(id)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engagements_create**
> Engagement engagements_create(data)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    data = defectdojo_openapi.Engagement() # Engagement | 

    try:
        api_response = api_instance.engagements_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Engagement**](Engagement.md)|  | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_delete**
> engagements_delete(id)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_instance.engagements_delete(id)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

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

# **engagements_generate_report**
> ReportGenerate engagements_generate_report(id, data)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
data = defectdojo_openapi.ReportGenerateOption() # ReportGenerateOption | 

    try:
        api_response = api_instance.engagements_generate_report(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
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

# **engagements_list**
> InlineResponse2002 engagements_list(id=id, active=active, eng_type=eng_type, target_start=target_start, target_end=target_end, requester=requester, report_type=report_type, updated=updated, threat_model=threat_model, api_test=api_test, pen_test=pen_test, status=status, product=product, name=name, version=version, limit=limit, offset=offset)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 3.4 # float |  (optional)
active = 'active_example' # str |  (optional)
eng_type = 'eng_type_example' # str |  (optional)
target_start = 'target_start_example' # str |  (optional)
target_end = 'target_end_example' # str |  (optional)
requester = 'requester_example' # str |  (optional)
report_type = 'report_type_example' # str |  (optional)
updated = 'updated_example' # str |  (optional)
threat_model = 'threat_model_example' # str |  (optional)
api_test = 'api_test_example' # str |  (optional)
pen_test = 'pen_test_example' # str |  (optional)
status = 'status_example' # str |  (optional)
product = 'product_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.engagements_list(id=id, active=active, eng_type=eng_type, target_start=target_start, target_end=target_end, requester=requester, report_type=report_type, updated=updated, threat_model=threat_model, api_test=api_test, pen_test=pen_test, status=status, product=product, name=name, version=version, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **active** | **str**|  | [optional] 
 **eng_type** | **str**|  | [optional] 
 **target_start** | **str**|  | [optional] 
 **target_end** | **str**|  | [optional] 
 **requester** | **str**|  | [optional] 
 **report_type** | **str**|  | [optional] 
 **updated** | **str**|  | [optional] 
 **threat_model** | **str**|  | [optional] 
 **api_test** | **str**|  | [optional] 
 **pen_test** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **engagements_partial_update**
> Engagement engagements_partial_update(id, data)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
data = defectdojo_openapi.Engagement() # Engagement | 

    try:
        api_response = api_instance.engagements_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **data** | [**Engagement**](Engagement.md)|  | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_read**
> Engagement engagements_read(id)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_response = api_instance.engagements_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

### Return type

[**Engagement**](Engagement.md)

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

# **engagements_reopen**
> engagements_reopen(id)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.

    try:
        api_instance.engagements_reopen(id)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_reopen: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engagements_update**
> Engagement engagements_update(id, data)



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
    api_instance = defectdojo_openapi.EngagementsApi(api_client)
    id = 56 # int | A unique integer value identifying this engagement.
data = defectdojo_openapi.Engagement() # Engagement | 

    try:
        api_response = api_instance.engagements_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngagementsApi->engagements_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this engagement. | 
 **data** | [**Engagement**](Engagement.md)|  | 

### Return type

[**Engagement**](Engagement.md)

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

