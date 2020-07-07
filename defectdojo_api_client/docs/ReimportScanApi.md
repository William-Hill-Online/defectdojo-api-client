# defectdojo_api_client.ReimportScanApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reimport_scan_create**](ReimportScanApi.md#reimport_scan_create) | **POST** /reimport-scan/ | 


# **reimport_scan_create**
> ReImportScan reimport_scan_create(scan_date, scan_type, test, minimum_severity=minimum_severity, active=active, verified=verified, endpoint_to_add=endpoint_to_add, file=file, push_to_jira=push_to_jira)



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import defectdojo_api_client
from defectdojo_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration = defectdojo_api_client.Configuration(
    host = "http://localhost:8080/api/v2",
    api_key = {
        'api_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with defectdojo_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = defectdojo_api_client.ReimportScanApi(api_client)
    scan_date = '2013-10-20' # date | 
scan_type = 'scan_type_example' # str | 
test = 56 # int | 
minimum_severity = 'Info' # str |  (optional) (default to 'Info')
active = True # bool |  (optional) (default to True)
verified = True # bool |  (optional) (default to True)
endpoint_to_add = 56 # int |  (optional)
file = '/path/to/file' # file |  (optional)
push_to_jira = False # bool |  (optional) (default to False)

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
 **minimum_severity** | **str**|  | [optional] [default to &#39;Info&#39;]
 **active** | **bool**|  | [optional] [default to True]
 **verified** | **bool**|  | [optional] [default to True]
 **endpoint_to_add** | **int**|  | [optional] 
 **file** | **file**|  | [optional] 
 **push_to_jira** | **bool**|  | [optional] [default to False]

### Return type

[**ReImportScan**](ReImportScan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

