# defectdojo_api_swagger.FindingTemplatesApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finding_templates_create**](FindingTemplatesApi.md#finding_templates_create) | **POST** /finding_templates/ | 
[**finding_templates_list**](FindingTemplatesApi.md#finding_templates_list) | **GET** /finding_templates/ | 
[**finding_templates_partial_update**](FindingTemplatesApi.md#finding_templates_partial_update) | **PATCH** /finding_templates/{id}/ | 
[**finding_templates_read**](FindingTemplatesApi.md#finding_templates_read) | **GET** /finding_templates/{id}/ | 
[**finding_templates_update**](FindingTemplatesApi.md#finding_templates_update) | **PUT** /finding_templates/{id}/ | 


# **finding_templates_create**
> FindingTemplate finding_templates_create(data)





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
api_instance = defectdojo_api_swagger.FindingTemplatesApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.FindingTemplate() # FindingTemplate | 

try:
    api_response = api_instance.finding_templates_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingTemplatesApi->finding_templates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FindingTemplate**](FindingTemplate.md)|  | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finding_templates_list**
> InlineResponse2003 finding_templates_list(id=id, title=title, cwe=cwe, severity=severity, description=description, mitigation=mitigation, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.FindingTemplatesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
title = 'title_example' # str |  (optional)
cwe = 8.14 # float |  (optional)
severity = 'severity_example' # str |  (optional)
description = 'description_example' # str |  (optional)
mitigation = 'mitigation_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.finding_templates_list(id=id, title=title, cwe=cwe, severity=severity, description=description, mitigation=mitigation, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingTemplatesApi->finding_templates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **title** | **str**|  | [optional] 
 **cwe** | **float**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **mitigation** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finding_templates_partial_update**
> FindingTemplate finding_templates_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.FindingTemplatesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding_ template.
data = defectdojo_api_swagger.FindingTemplate() # FindingTemplate | 

try:
    api_response = api_instance.finding_templates_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingTemplatesApi->finding_templates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 
 **data** | [**FindingTemplate**](FindingTemplate.md)|  | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finding_templates_read**
> FindingTemplate finding_templates_read(id)





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
api_instance = defectdojo_api_swagger.FindingTemplatesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding_ template.

try:
    api_response = api_instance.finding_templates_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingTemplatesApi->finding_templates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finding_templates_update**
> FindingTemplate finding_templates_update(id, data)





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
api_instance = defectdojo_api_swagger.FindingTemplatesApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding_ template.
data = defectdojo_api_swagger.FindingTemplate() # FindingTemplate | 

try:
    api_response = api_instance.finding_templates_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingTemplatesApi->finding_templates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding_ template. | 
 **data** | [**FindingTemplate**](FindingTemplate.md)|  | 

### Return type

[**FindingTemplate**](FindingTemplate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

