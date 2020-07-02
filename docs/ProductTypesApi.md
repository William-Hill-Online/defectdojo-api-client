# defectdojo_openapi.ProductTypesApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_types_create**](ProductTypesApi.md#product_types_create) | **POST** /product_types/ | 
[**product_types_generate_report**](ProductTypesApi.md#product_types_generate_report) | **POST** /product_types/{id}/generate_report/ | 
[**product_types_list**](ProductTypesApi.md#product_types_list) | **GET** /product_types/ | 
[**product_types_partial_update**](ProductTypesApi.md#product_types_partial_update) | **PATCH** /product_types/{id}/ | 
[**product_types_read**](ProductTypesApi.md#product_types_read) | **GET** /product_types/{id}/ | 
[**product_types_update**](ProductTypesApi.md#product_types_update) | **PUT** /product_types/{id}/ | 


# **product_types_create**
> ProductType product_types_create(data)



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
    api_instance = defectdojo_openapi.ProductTypesApi(api_client)
    data = defectdojo_openapi.ProductType() # ProductType | 

    try:
        api_response = api_instance.product_types_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductTypesApi->product_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_generate_report**
> ReportGenerate product_types_generate_report(id, data)



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
    api_instance = defectdojo_openapi.ProductTypesApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ type.
data = defectdojo_openapi.ReportGenerateOption() # ReportGenerateOption | 

    try:
        api_response = api_instance.product_types_generate_report(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductTypesApi->product_types_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 
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

# **product_types_list**
> InlineResponse20011 product_types_list(id=id, name=name, critical_product=critical_product, key_product=key_product, created=created, updated=updated, limit=limit, offset=offset)



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
    api_instance = defectdojo_openapi.ProductTypesApi(api_client)
    id = 3.4 # float |  (optional)
name = 'name_example' # str |  (optional)
critical_product = 'critical_product_example' # str |  (optional)
key_product = 'key_product_example' # str |  (optional)
created = 'created_example' # str |  (optional)
updated = 'updated_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

    try:
        api_response = api_instance.product_types_list(id=id, name=name, critical_product=critical_product, key_product=key_product, created=created, updated=updated, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductTypesApi->product_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **critical_product** | **str**|  | [optional] 
 **key_product** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **updated** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

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

# **product_types_partial_update**
> ProductType product_types_partial_update(id, data)



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
    api_instance = defectdojo_openapi.ProductTypesApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ type.
data = defectdojo_openapi.ProductType() # ProductType | 

    try:
        api_response = api_instance.product_types_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductTypesApi->product_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_read**
> ProductType product_types_read(id)



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
    api_instance = defectdojo_openapi.ProductTypesApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ type.

    try:
        api_response = api_instance.product_types_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductTypesApi->product_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_update**
> ProductType product_types_update(id, data)



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
    api_instance = defectdojo_openapi.ProductTypesApi(api_client)
    id = 56 # int | A unique integer value identifying this product_ type.
data = defectdojo_openapi.ProductType() # ProductType | 

    try:
        api_response = api_instance.product_types_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductTypesApi->product_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

