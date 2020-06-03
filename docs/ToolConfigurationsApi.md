# defectdojo_api_swagger.ToolConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tool_configurations_create**](ToolConfigurationsApi.md#tool_configurations_create) | **POST** /tool_configurations/ | 
[**tool_configurations_delete**](ToolConfigurationsApi.md#tool_configurations_delete) | **DELETE** /tool_configurations/{id}/ | 
[**tool_configurations_list**](ToolConfigurationsApi.md#tool_configurations_list) | **GET** /tool_configurations/ | 
[**tool_configurations_partial_update**](ToolConfigurationsApi.md#tool_configurations_partial_update) | **PATCH** /tool_configurations/{id}/ | 
[**tool_configurations_read**](ToolConfigurationsApi.md#tool_configurations_read) | **GET** /tool_configurations/{id}/ | 
[**tool_configurations_update**](ToolConfigurationsApi.md#tool_configurations_update) | **PUT** /tool_configurations/{id}/ | 


# **tool_configurations_create**
> ToolConfiguration tool_configurations_create(data)





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
api_instance = defectdojo_api_swagger.ToolConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.ToolConfiguration() # ToolConfiguration | 

try:
    api_response = api_instance.tool_configurations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ToolConfiguration**](ToolConfiguration.md)|  | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_configurations_delete**
> tool_configurations_delete(id)





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
api_instance = defectdojo_api_swagger.ToolConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.

try:
    api_instance.tool_configurations_delete(id)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_configurations_list**
> InlineResponse20018 tool_configurations_list(id=id, name=name, tool_type=tool_type, url=url, authentication_type=authentication_type, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.ToolConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
name = 'name_example' # str |  (optional)
tool_type = 'tool_type_example' # str |  (optional)
url = 'url_example' # str |  (optional)
authentication_type = 'authentication_type_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tool_configurations_list(id=id, name=name, tool_type=tool_type, url=url, authentication_type=authentication_type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **tool_type** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **authentication_type** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_configurations_partial_update**
> ToolConfiguration tool_configurations_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.ToolConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.
data = defectdojo_api_swagger.ToolConfiguration() # ToolConfiguration | 

try:
    api_response = api_instance.tool_configurations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 
 **data** | [**ToolConfiguration**](ToolConfiguration.md)|  | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_configurations_read**
> ToolConfiguration tool_configurations_read(id)





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
api_instance = defectdojo_api_swagger.ToolConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.

try:
    api_response = api_instance.tool_configurations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_configurations_update**
> ToolConfiguration tool_configurations_update(id, data)





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
api_instance = defectdojo_api_swagger.ToolConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.
data = defectdojo_api_swagger.ToolConfiguration() # ToolConfiguration | 

try:
    api_response = api_instance.tool_configurations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 
 **data** | [**ToolConfiguration**](ToolConfiguration.md)|  | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

