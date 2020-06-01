# defectdojo_api_swagger.NotesApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notes_list**](NotesApi.md#notes_list) | **GET** /notes/ | 
[**notes_partial_update**](NotesApi.md#notes_partial_update) | **PATCH** /notes/{id}/ | 
[**notes_read**](NotesApi.md#notes_read) | **GET** /notes/{id}/ | 
[**notes_update**](NotesApi.md#notes_update) | **PUT** /notes/{id}/ | 


# **notes_list**
> InlineResponse20010 notes_list(id=id, entry=entry, author=author, private=private, _date=_date, edited=edited, edit_time=edit_time, editor=editor, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.NotesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
entry = 'entry_example' # str |  (optional)
author = 'author_example' # str |  (optional)
private = 'private_example' # str |  (optional)
_date = '_date_example' # str |  (optional)
edited = 'edited_example' # str |  (optional)
edit_time = 'edit_time_example' # str |  (optional)
editor = 'editor_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.notes_list(id=id, entry=entry, author=author, private=private, _date=_date, edited=edited, edit_time=edit_time, editor=editor, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **entry** | **str**|  | [optional] 
 **author** | **str**|  | [optional] 
 **private** | **str**|  | [optional] 
 **_date** | **str**|  | [optional] 
 **edited** | **str**|  | [optional] 
 **edit_time** | **str**|  | [optional] 
 **editor** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_partial_update**
> Note notes_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.NotesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this notes.
data = defectdojo_api_swagger.Note() # Note | 

try:
    api_response = api_instance.notes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notes. | 
 **data** | [**Note**](Note.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_read**
> Note notes_read(id)





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
api_instance = defectdojo_api_swagger.NotesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this notes.

try:
    api_response = api_instance.notes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notes. | 

### Return type

[**Note**](Note.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_update**
> Note notes_update(id, data)





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
api_instance = defectdojo_api_swagger.NotesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this notes.
data = defectdojo_api_swagger.Note() # Note | 

try:
    api_response = api_instance.notes_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->notes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this notes. | 
 **data** | [**Note**](Note.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

