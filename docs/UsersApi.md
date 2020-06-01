# defectdojo_api_swagger.UsersApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_list**](UsersApi.md#users_list) | **GET** /users/ | 
[**users_read**](UsersApi.md#users_read) | **GET** /users/{id}/ | 


# **users_list**
> InlineResponse20021 users_list(id=id, username=username, first_name=first_name, last_name=last_name, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.UsersApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
username = 'username_example' # str |  (optional)
first_name = 'first_name_example' # str |  (optional)
last_name = 'last_name_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.users_list(id=id, username=username, first_name=first_name, last_name=last_name, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **username** | **str**|  | [optional] 
 **first_name** | **str**|  | [optional] 
 **last_name** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_read**
> User users_read(id)





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
api_instance = defectdojo_api_swagger.UsersApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this user.

try:
    api_response = api_instance.users_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user. | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

