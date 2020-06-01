# defectdojo_api_swagger.EndpointsApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_create**](EndpointsApi.md#endpoints_create) | **POST** /endpoints/ | 
[**endpoints_delete**](EndpointsApi.md#endpoints_delete) | **DELETE** /endpoints/{id}/ | 
[**endpoints_generate_report**](EndpointsApi.md#endpoints_generate_report) | **POST** /endpoints/{id}/generate_report/ | 
[**endpoints_list**](EndpointsApi.md#endpoints_list) | **GET** /endpoints/ | 
[**endpoints_partial_update**](EndpointsApi.md#endpoints_partial_update) | **PATCH** /endpoints/{id}/ | 
[**endpoints_read**](EndpointsApi.md#endpoints_read) | **GET** /endpoints/{id}/ | 
[**endpoints_update**](EndpointsApi.md#endpoints_update) | **PUT** /endpoints/{id}/ | 


# **endpoints_create**
> Endpoint endpoints_create(data)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.Endpoint() # Endpoint | 

try:
    api_response = api_instance.endpoints_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Endpoint**](Endpoint.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_delete**
> endpoints_delete(id)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this endpoint.

try:
    api_instance.endpoints_delete(id)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_generate_report**
> Endpoint endpoints_generate_report(id, data)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this endpoint.
data = defectdojo_api_swagger.Endpoint() # Endpoint | 

try:
    api_response = api_instance.endpoints_generate_report(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
 **data** | [**Endpoint**](Endpoint.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_list**
> InlineResponse2001 endpoints_list(id=id, host=host, product=product, limit=limit, offset=offset)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
host = 'host_example' # str |  (optional)
product = 'product_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.endpoints_list(id=id, host=host, product=product, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **host** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_partial_update**
> Endpoint endpoints_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this endpoint.
data = defectdojo_api_swagger.Endpoint() # Endpoint | 

try:
    api_response = api_instance.endpoints_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
 **data** | [**Endpoint**](Endpoint.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_read**
> Endpoint endpoints_read(id)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this endpoint.

try:
    api_response = api_instance.endpoints_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_update**
> Endpoint endpoints_update(id, data)





### Example
```python
from __future__ import print_function
import time
import defectdojo_api_swagger
from defectdojo_api_swagger.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = defectdojo_api_swagger.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = defectdojo_api_swagger.EndpointsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this endpoint.
data = defectdojo_api_swagger.Endpoint() # Endpoint | 

try:
    api_response = api_instance.endpoints_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->endpoints_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this endpoint. | 
 **data** | [**Endpoint**](Endpoint.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

