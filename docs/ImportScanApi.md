# defectdojo_api_swagger.ImportScanApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_scan_create**](ImportScanApi.md#import_scan_create) | **POST** /import-scan/ | 


# **import_scan_create**
> ImportScan import_scan_create(scan_type, engagement, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, test_type=test_type, file=file, lead=lead, tags=tags, close_old_findings=close_old_findings, push_to_jira=push_to_jira)





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
api_instance = defectdojo_api_swagger.ImportScanApi(defectdojo_api_swagger.ApiClient(configuration))
scan_type = 'scan_type_example' # str | 
engagement = 56 # int | 
scan_date = '2020-06-05' # date |  (optional) (default to 2020-06-05)
minimum_severity = 'Info' # str |  (optional) (default to Info)
active = true # bool |  (optional) (default to true)
verified = true # bool |  (optional) (default to true)
endpoint_to_add = 56 # int |  (optional)
test_type = 'test_type_example' # str |  (optional)
file = '/path/to/file.txt' # file |  (optional)
lead = 56 # int |  (optional)
tags = ['tags_example'] # list[str] |  (optional)
close_old_findings = false # bool |  (optional) (default to false)
push_to_jira = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.import_scan_create(scan_type, engagement, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, test_type=test_type, file=file, lead=lead, tags=tags, close_old_findings=close_old_findings, push_to_jira=push_to_jira)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportScanApi->import_scan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_type** | **str**|  | 
 **engagement** | **int**|  | 
 **scan_date** | **date**|  | [optional] [default to 2020-06-05]
 **minimum_severity** | **str**|  | [optional] [default to Info]
 **active** | **bool**|  | [optional] [default to true]
 **verified** | **bool**|  | [optional] [default to true]
 **endpoint_to_add** | **int**|  | [optional] 
 **test_type** | **str**|  | [optional] 
 **file** | **file**|  | [optional] 
 **lead** | **int**|  | [optional] 
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **close_old_findings** | **bool**|  | [optional] [default to false]
 **push_to_jira** | **bool**|  | [optional] [default to false]

### Return type

[**ImportScan**](ImportScan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

