# defectdojo_api_swagger.StubFindingsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stub_findings_create**](StubFindingsApi.md#stub_findings_create) | **POST** /stub_findings/ | 
[**stub_findings_list**](StubFindingsApi.md#stub_findings_list) | **GET** /stub_findings/ | 
[**stub_findings_partial_update**](StubFindingsApi.md#stub_findings_partial_update) | **PATCH** /stub_findings/{id}/ | 
[**stub_findings_read**](StubFindingsApi.md#stub_findings_read) | **GET** /stub_findings/{id}/ | 
[**stub_findings_update**](StubFindingsApi.md#stub_findings_update) | **PUT** /stub_findings/{id}/ | 


# **stub_findings_create**
> StubFindingCreate stub_findings_create(data)





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
api_instance = defectdojo_api_swagger.StubFindingsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.StubFindingCreate() # StubFindingCreate | 

try:
    api_response = api_instance.stub_findings_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StubFindingsApi->stub_findings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**StubFindingCreate**](StubFindingCreate.md)|  | 

### Return type

[**StubFindingCreate**](StubFindingCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stub_findings_list**
> InlineResponse20015 stub_findings_list(id=id, title=title, _date=_date, severity=severity, description=description, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.StubFindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
title = 'title_example' # str |  (optional)
_date = '_date_example' # str |  (optional)
severity = 'severity_example' # str |  (optional)
description = 'description_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.stub_findings_list(id=id, title=title, _date=_date, severity=severity, description=description, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StubFindingsApi->stub_findings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **title** | **str**|  | [optional] 
 **_date** | **str**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stub_findings_partial_update**
> StubFinding stub_findings_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.StubFindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this stub_ finding.
data = defectdojo_api_swagger.StubFinding() # StubFinding | 

try:
    api_response = api_instance.stub_findings_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StubFindingsApi->stub_findings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stub_ finding. | 
 **data** | [**StubFinding**](StubFinding.md)|  | 

### Return type

[**StubFinding**](StubFinding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stub_findings_read**
> StubFinding stub_findings_read(id)





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
api_instance = defectdojo_api_swagger.StubFindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this stub_ finding.

try:
    api_response = api_instance.stub_findings_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StubFindingsApi->stub_findings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stub_ finding. | 

### Return type

[**StubFinding**](StubFinding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stub_findings_update**
> StubFinding stub_findings_update(id, data)





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
api_instance = defectdojo_api_swagger.StubFindingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this stub_ finding.
data = defectdojo_api_swagger.StubFinding() # StubFinding | 

try:
    api_response = api_instance.stub_findings_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StubFindingsApi->stub_findings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stub_ finding. | 
 **data** | [**StubFinding**](StubFinding.md)|  | 

### Return type

[**StubFinding**](StubFinding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

