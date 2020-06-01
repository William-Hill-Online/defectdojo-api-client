# defectdojo_api_swagger.FindingsApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findings_accept_risks**](FindingsApi.md#findings_accept_risks) | **POST** /findings/accept_risks/ | 
[**findings_create**](FindingsApi.md#findings_create) | **POST** /findings/ | 
[**findings_delete**](FindingsApi.md#findings_delete) | **DELETE** /findings/{id}/ | 
[**findings_generate_report**](FindingsApi.md#findings_generate_report) | **POST** /findings/generate_report/ | 
[**findings_list**](FindingsApi.md#findings_list) | **GET** /findings/ | 
[**findings_notes_create**](FindingsApi.md#findings_notes_create) | **POST** /findings/{id}/notes/ | 
[**findings_notes_partial_update**](FindingsApi.md#findings_notes_partial_update) | **PATCH** /findings/{id}/notes/ | 
[**findings_notes_read**](FindingsApi.md#findings_notes_read) | **GET** /findings/{id}/notes/ | 
[**findings_partial_update**](FindingsApi.md#findings_partial_update) | **PATCH** /findings/{id}/ | 
[**findings_read**](FindingsApi.md#findings_read) | **GET** /findings/{id}/ | 
[**findings_remove_note**](FindingsApi.md#findings_remove_note) | **PATCH** /findings/{id}/remove_note/ | 
[**findings_remove_tags_partial_update**](FindingsApi.md#findings_remove_tags_partial_update) | **PATCH** /findings/{id}/remove_tags/ | 
[**findings_remove_tags_update**](FindingsApi.md#findings_remove_tags_update) | **PUT** /findings/{id}/remove_tags/ | 
[**findings_tags_create**](FindingsApi.md#findings_tags_create) | **POST** /findings/{id}/tags/ | 
[**findings_tags_read**](FindingsApi.md#findings_tags_read) | **GET** /findings/{id}/tags/ | 
[**findings_update**](FindingsApi.md#findings_update) | **PUT** /findings/{id}/ | 


# **findings_accept_risks**
> FindingCreate findings_accept_risks(data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.FindingCreate() # FindingCreate | 

try:
    api_response = api_instance.findings_accept_risks(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_accept_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FindingCreate**](FindingCreate.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_create**
> FindingCreate findings_create(data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.FindingCreate() # FindingCreate | 

try:
    api_response = api_instance.findings_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FindingCreate**](FindingCreate.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_delete**
> findings_delete(id)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.

try:
    api_instance.findings_delete(id)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_generate_report**
> FindingCreate findings_generate_report(data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.FindingCreate() # FindingCreate | 

try:
    api_response = api_instance.findings_generate_report(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**FindingCreate**](FindingCreate.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_list**
> InlineResponse2004 findings_list(id=id, title=title, _date=_date, severity=severity, description=description, mitigated=mitigated, endpoints=endpoints, test=test, active=active, verified=verified, false_p=false_p, reporter=reporter, url=url, out_of_scope=out_of_scope, duplicate=duplicate, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
title = 'title_example' # str |  (optional)
_date = '_date_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
description = 'description_example' # str |  (optional)
mitigated = 'mitigated_example' # str |  (optional)
endpoints = 'endpoints_example' # str |  (optional)
test = 'test_example' # str |  (optional)
active = 'active_example' # str |  (optional)
verified = 'verified_example' # str |  (optional)
false_p = 'false_p_example' # str |  (optional)
reporter = 'reporter_example' # str |  (optional)
url = 'url_example' # str |  (optional)
out_of_scope = 'out_of_scope_example' # str |  (optional)
duplicate = 'duplicate_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.findings_list(id=id, title=title, _date=_date, severity=severity, description=description, mitigated=mitigated, endpoints=endpoints, test=test, active=active, verified=verified, false_p=false_p, reporter=reporter, url=url, out_of_scope=out_of_scope, duplicate=duplicate, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **title** | **str**|  | [optional] 
 **_date** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **mitigated** | **str**|  | [optional] 
 **endpoints** | **str**|  | [optional] 
 **test** | **str**|  | [optional] 
 **active** | **str**|  | [optional] 
 **verified** | **str**|  | [optional] 
 **false_p** | **str**|  | [optional] 
 **reporter** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **out_of_scope** | **str**|  | [optional] 
 **duplicate** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_notes_create**
> FindingCreate findings_notes_create(id, data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.FindingCreate() # FindingCreate | 

try:
    api_response = api_instance.findings_notes_create(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**FindingCreate**](FindingCreate.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_notes_partial_update**
> Finding findings_notes_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.Finding() # Finding | 

try:
    api_response = api_instance.findings_notes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_notes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_notes_read**
> Finding findings_notes_read(id)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.

try:
    api_response = api_instance.findings_notes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_notes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_partial_update**
> Finding findings_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.Finding() # Finding | 

try:
    api_response = api_instance.findings_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_read**
> Finding findings_read(id)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.

try:
    api_response = api_instance.findings_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_note**
> Note findings_remove_note(id, data)



Remove Note From Finding Note

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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.Note() # Note | 

try:
    api_response = api_instance.findings_remove_note(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_remove_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Note**](Note.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_tags_partial_update**
> Finding findings_remove_tags_partial_update(id, data)



Remove Tag(s) from finding list of tags

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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.Finding() # Finding | 

try:
    api_response = api_instance.findings_remove_tags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_remove_tags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_remove_tags_update**
> Finding findings_remove_tags_update(id, data)



Remove Tag(s) from finding list of tags

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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.Finding() # Finding | 

try:
    api_response = api_instance.findings_remove_tags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_remove_tags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_tags_create**
> FindingCreate findings_tags_create(id, data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.FindingCreate() # FindingCreate | 

try:
    api_response = api_instance.findings_tags_create(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**FindingCreate**](FindingCreate.md)|  | 

### Return type

[**FindingCreate**](FindingCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_tags_read**
> Finding findings_tags_read(id)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.

try:
    api_response = api_instance.findings_tags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findings_update**
> Finding findings_update(id, data)





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
api_instance = defectdojo_api_swagger.FindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this finding.
data = defectdojo_api_swagger.Finding() # Finding | 

try:
    api_response = api_instance.findings_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FindingsApi->findings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this finding. | 
 **data** | [**Finding**](Finding.md)|  | 

### Return type

[**Finding**](Finding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

