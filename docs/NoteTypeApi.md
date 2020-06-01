# defectdojo_api_swagger.NoteTypeApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**note_type_create**](NoteTypeApi.md#note_type_create) | **POST** /note_type/ | 
[**note_type_delete**](NoteTypeApi.md#note_type_delete) | **DELETE** /note_type/{id}/ | 
[**note_type_list**](NoteTypeApi.md#note_type_list) | **GET** /note_type/ | 
[**note_type_partial_update**](NoteTypeApi.md#note_type_partial_update) | **PATCH** /note_type/{id}/ | 
[**note_type_read**](NoteTypeApi.md#note_type_read) | **GET** /note_type/{id}/ | 
[**note_type_update**](NoteTypeApi.md#note_type_update) | **PUT** /note_type/{id}/ | 


# **note_type_create**
> NoteType note_type_create(data)





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
api_instance = defectdojo_api_swagger.NoteTypeApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.NoteType() # NoteType | 

try:
    api_response = api_instance.note_type_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteTypeApi->note_type_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**NoteType**](NoteType.md)|  | 

### Return type

[**NoteType**](NoteType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_type_delete**
> note_type_delete(id)





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
api_instance = defectdojo_api_swagger.NoteTypeApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this note_ type.

try:
    api_instance.note_type_delete(id)
except ApiException as e:
    print("Exception when calling NoteTypeApi->note_type_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note_ type. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_type_list**
> InlineResponse2009 note_type_list(id=id, name=name, description=description, is_single=is_single, is_active=is_active, is_mandatory=is_mandatory, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.NoteTypeApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
is_single = 'is_single_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
is_mandatory = 'is_mandatory_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.note_type_list(id=id, name=name, description=description, is_single=is_single, is_active=is_active, is_mandatory=is_mandatory, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteTypeApi->note_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **is_single** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **is_mandatory** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_type_partial_update**
> NoteType note_type_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.NoteTypeApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this note_ type.
data = defectdojo_api_swagger.NoteType() # NoteType | 

try:
    api_response = api_instance.note_type_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteTypeApi->note_type_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note_ type. | 
 **data** | [**NoteType**](NoteType.md)|  | 

### Return type

[**NoteType**](NoteType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_type_read**
> NoteType note_type_read(id)





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
api_instance = defectdojo_api_swagger.NoteTypeApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this note_ type.

try:
    api_response = api_instance.note_type_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteTypeApi->note_type_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note_ type. | 

### Return type

[**NoteType**](NoteType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **note_type_update**
> NoteType note_type_update(id, data)





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
api_instance = defectdojo_api_swagger.NoteTypeApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this note_ type.
data = defectdojo_api_swagger.NoteType() # NoteType | 

try:
    api_response = api_instance.note_type_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteTypeApi->note_type_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note_ type. | 
 **data** | [**NoteType**](NoteType.md)|  | 

### Return type

[**NoteType**](NoteType.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

