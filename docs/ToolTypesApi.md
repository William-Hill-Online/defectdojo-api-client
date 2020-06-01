# defectdojo_api_swagger.ToolTypesApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tool_types_create**](ToolTypesApi.md#tool_types_create) | **POST** /tool_types/ | 
[**tool_types_delete**](ToolTypesApi.md#tool_types_delete) | **DELETE** /tool_types/{id}/ | 
[**tool_types_list**](ToolTypesApi.md#tool_types_list) | **GET** /tool_types/ | 
[**tool_types_partial_update**](ToolTypesApi.md#tool_types_partial_update) | **PATCH** /tool_types/{id}/ | 
[**tool_types_read**](ToolTypesApi.md#tool_types_read) | **GET** /tool_types/{id}/ | 
[**tool_types_update**](ToolTypesApi.md#tool_types_update) | **PUT** /tool_types/{id}/ | 


# **tool_types_create**
> ToolType tool_types_create(data)





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
api_instance = defectdojo_api_swagger.ToolTypesApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.ToolType() # ToolType | 

try:
    api_response = api_instance.tool_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolTypesApi->tool_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ToolType**](ToolType.md)|  | 

### Return type

[**ToolType**](ToolType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_types_delete**
> tool_types_delete(id)





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
api_instance = defectdojo_api_swagger.ToolTypesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ type.

try:
    api_instance.tool_types_delete(id)
except ApiException as e:
    print("Exception when calling ToolTypesApi->tool_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ type. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_types_list**
> InlineResponse20020 tool_types_list(id=id, name=name, description=description, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.ToolTypesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tool_types_list(id=id, name=name, description=description, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolTypesApi->tool_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_types_partial_update**
> ToolType tool_types_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.ToolTypesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ type.
data = defectdojo_api_swagger.ToolType() # ToolType | 

try:
    api_response = api_instance.tool_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolTypesApi->tool_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ type. | 
 **data** | [**ToolType**](ToolType.md)|  | 

### Return type

[**ToolType**](ToolType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_types_read**
> ToolType tool_types_read(id)





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
api_instance = defectdojo_api_swagger.ToolTypesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ type.

try:
    api_response = api_instance.tool_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolTypesApi->tool_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ type. | 

### Return type

[**ToolType**](ToolType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_types_update**
> ToolType tool_types_update(id, data)





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
api_instance = defectdojo_api_swagger.ToolTypesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ type.
data = defectdojo_api_swagger.ToolType() # ToolType | 

try:
    api_response = api_instance.tool_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolTypesApi->tool_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ type. | 
 **data** | [**ToolType**](ToolType.md)|  | 

### Return type

[**ToolType**](ToolType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

