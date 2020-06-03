# defectdojo_api_swagger.ReimportScanApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reimport_scan_create**](ReimportScanApi.md#reimport_scan_create) | **POST** /reimport-scan/ | 


# **reimport_scan_create**
> ReImportScan reimport_scan_create(scan_date, scan_type, test, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, push_to_jira=push_to_jira)





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
api_instance = defectdojo_api_swagger.ReimportScanApi(defectdojo_api_swagger.ApiClient(configuration))
scan_date = '2013-10-20' # date | 
scan_type = 'scan_type_example' # str | 
test = 56 # int | 
minimum_severity = 'Info' # str |  (optional) (default to Info)
active = true # bool |  (optional) (default to true)
verified = true # bool |  (optional) (default to true)
endpoint_to_add = 56 # int |  (optional)
file = '/path/to/file.txt' # file |  (optional)
push_to_jira = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.reimport_scan_create(scan_date, scan_type, test, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, push_to_jira=push_to_jira)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReimportScanApi->reimport_scan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_date** | **date**|  | 
 **scan_type** | **str**|  | 
 **test** | **int**|  | 
 **minimum_severity** | **str**|  | [optional] [default to Info]
 **active** | **bool**|  | [optional] [default to true]
 **verified** | **bool**|  | [optional] [default to true]
 **endpoint_to_add** | **int**|  | [optional] 
 **file** | **file**|  | [optional] 
 **push_to_jira** | **bool**|  | [optional] [default to false]

### Return type

[**ReImportScan**](ReImportScan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

