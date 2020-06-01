# defectdojo_api_swagger.MetadataApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_create**](MetadataApi.md#metadata_create) | **POST** /metadata/ | 
[**metadata_delete**](MetadataApi.md#metadata_delete) | **DELETE** /metadata/{id}/ | 
[**metadata_list**](MetadataApi.md#metadata_list) | **GET** /metadata/ | 
[**metadata_partial_update**](MetadataApi.md#metadata_partial_update) | **PATCH** /metadata/{id}/ | 
[**metadata_read**](MetadataApi.md#metadata_read) | **GET** /metadata/{id}/ | 
[**metadata_update**](MetadataApi.md#metadata_update) | **PUT** /metadata/{id}/ | 


# **metadata_create**
> Meta metadata_create(data)





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
api_instance = defectdojo_api_swagger.MetadataApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.Meta() # Meta | 

try:
    api_response = api_instance.metadata_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Meta**](Meta.md)|  | 

### Return type

[**Meta**](Meta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_delete**
> metadata_delete(id)





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
api_instance = defectdojo_api_swagger.MetadataApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this dojo meta.

try:
    api_instance.metadata_delete(id)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this dojo meta. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_list**
> InlineResponse2008 metadata_list(id=id, product=product, endpoint=endpoint, name=name, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.MetadataApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
product = 'product_example' # str |  (optional)
endpoint = 'endpoint_example' # str |  (optional)
name = 'name_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.metadata_list(id=id, product=product, endpoint=endpoint, name=name, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **product** | **str**|  | [optional] 
 **endpoint** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_partial_update**
> Meta metadata_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.MetadataApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this dojo meta.
data = defectdojo_api_swagger.Meta() # Meta | 

try:
    api_response = api_instance.metadata_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this dojo meta. | 
 **data** | [**Meta**](Meta.md)|  | 

### Return type

[**Meta**](Meta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_read**
> Meta metadata_read(id)





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
api_instance = defectdojo_api_swagger.MetadataApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this dojo meta.

try:
    api_response = api_instance.metadata_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this dojo meta. | 

### Return type

[**Meta**](Meta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_update**
> Meta metadata_update(id, data)





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
api_instance = defectdojo_api_swagger.MetadataApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this dojo meta.
data = defectdojo_api_swagger.Meta() # Meta | 

try:
    api_response = api_instance.metadata_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this dojo meta. | 
 **data** | [**Meta**](Meta.md)|  | 

### Return type

[**Meta**](Meta.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

