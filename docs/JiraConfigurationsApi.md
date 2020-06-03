# defectdojo_api_swagger.JiraConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_configurations_create**](JiraConfigurationsApi.md#jira_configurations_create) | **POST** /jira_configurations/ | 
[**jira_configurations_delete**](JiraConfigurationsApi.md#jira_configurations_delete) | **DELETE** /jira_configurations/{id}/ | 
[**jira_configurations_list**](JiraConfigurationsApi.md#jira_configurations_list) | **GET** /jira_configurations/ | 
[**jira_configurations_partial_update**](JiraConfigurationsApi.md#jira_configurations_partial_update) | **PATCH** /jira_configurations/{id}/ | 
[**jira_configurations_read**](JiraConfigurationsApi.md#jira_configurations_read) | **GET** /jira_configurations/{id}/ | 
[**jira_configurations_update**](JiraConfigurationsApi.md#jira_configurations_update) | **PUT** /jira_configurations/{id}/ | 


# **jira_configurations_create**
> JIRAConf jira_configurations_create(data)





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
api_instance = defectdojo_api_swagger.JiraConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.JIRAConf() # JIRAConf | 

try:
    api_response = api_instance.jira_configurations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_configurations_delete**
> jira_configurations_delete(id)





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
api_instance = defectdojo_api_swagger.JiraConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.

try:
    api_instance.jira_configurations_delete(id)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_configurations_list**
> InlineResponse2005 jira_configurations_list(id=id, url=url, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.JiraConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
url = 'url_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.jira_configurations_list(id=id, url=url, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **url** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_configurations_partial_update**
> JIRAConf jira_configurations_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.JiraConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.
data = defectdojo_api_swagger.JIRAConf() # JIRAConf | 

try:
    api_response = api_instance.jira_configurations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_configurations_read**
> JIRAConf jira_configurations_read(id)





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
api_instance = defectdojo_api_swagger.JiraConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.

try:
    api_response = api_instance.jira_configurations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 

### Return type

[**JIRAConf**](JIRAConf.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_configurations_update**
> JIRAConf jira_configurations_update(id, data)





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
api_instance = defectdojo_api_swagger.JiraConfigurationsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.
data = defectdojo_api_swagger.JIRAConf() # JIRAConf | 

try:
    api_response = api_instance.jira_configurations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

