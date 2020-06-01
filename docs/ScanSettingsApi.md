# defectdojo_api_swagger.ScanSettingsApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan_settings_create**](ScanSettingsApi.md#scan_settings_create) | **POST** /scan_settings/ | 
[**scan_settings_delete**](ScanSettingsApi.md#scan_settings_delete) | **DELETE** /scan_settings/{id}/ | 
[**scan_settings_list**](ScanSettingsApi.md#scan_settings_list) | **GET** /scan_settings/ | 
[**scan_settings_partial_update**](ScanSettingsApi.md#scan_settings_partial_update) | **PATCH** /scan_settings/{id}/ | 
[**scan_settings_read**](ScanSettingsApi.md#scan_settings_read) | **GET** /scan_settings/{id}/ | 
[**scan_settings_update**](ScanSettingsApi.md#scan_settings_update) | **PUT** /scan_settings/{id}/ | 


# **scan_settings_create**
> ScanSettingsCreate scan_settings_create(data)





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
api_instance = defectdojo_api_swagger.ScanSettingsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.ScanSettingsCreate() # ScanSettingsCreate | 

try:
    api_response = api_instance.scan_settings_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ScanSettingsCreate**](ScanSettingsCreate.md)|  | 

### Return type

[**ScanSettingsCreate**](ScanSettingsCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_delete**
> scan_settings_delete(id)





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
api_instance = defectdojo_api_swagger.ScanSettingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.

try:
    api_instance.scan_settings_delete(id)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_list**
> InlineResponse20013 scan_settings_list(id=id, _date=_date, user=user, frequency=frequency, product=product, addresses=addresses, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.ScanSettingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
_date = '_date_example' # str |  (optional)
user = 'user_example' # str |  (optional)
frequency = 'frequency_example' # str |  (optional)
product = 'product_example' # str |  (optional)
addresses = 'addresses_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.scan_settings_list(id=id, _date=_date, user=user, frequency=frequency, product=product, addresses=addresses, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **_date** | **str**|  | [optional] 
 **user** | **str**|  | [optional] 
 **frequency** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **addresses** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_partial_update**
> ScanSettings scan_settings_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.ScanSettingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.
data = defectdojo_api_swagger.ScanSettings() # ScanSettings | 

try:
    api_response = api_instance.scan_settings_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 
 **data** | [**ScanSettings**](ScanSettings.md)|  | 

### Return type

[**ScanSettings**](ScanSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_read**
> ScanSettings scan_settings_read(id)





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
api_instance = defectdojo_api_swagger.ScanSettingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.

try:
    api_response = api_instance.scan_settings_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 

### Return type

[**ScanSettings**](ScanSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_update**
> ScanSettings scan_settings_update(id, data)





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
api_instance = defectdojo_api_swagger.ScanSettingsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.
data = defectdojo_api_swagger.ScanSettings() # ScanSettings | 

try:
    api_response = api_instance.scan_settings_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 
 **data** | [**ScanSettings**](ScanSettings.md)|  | 

### Return type

[**ScanSettings**](ScanSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

