# defectdojo_api_swagger.ProductsApi

All URIs are relative to *http://defectdojo.site.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_create**](ProductsApi.md#products_create) | **POST** /products/ | 
[**products_generate_report**](ProductsApi.md#products_generate_report) | **POST** /products/{id}/generate_report/ | 
[**products_list**](ProductsApi.md#products_list) | **GET** /products/ | 
[**products_partial_update**](ProductsApi.md#products_partial_update) | **PATCH** /products/{id}/ | 
[**products_read**](ProductsApi.md#products_read) | **GET** /products/{id}/ | 
[**products_update**](ProductsApi.md#products_update) | **PUT** /products/{id}/ | 


# **products_create**
> Product products_create(data)





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
api_instance = defectdojo_api_swagger.ProductsApi(defectdojo_api_swagger.ApiClient(configuration))
data = defectdojo_api_swagger.Product() # Product | 

try:
    api_response = api_instance.products_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_generate_report**
> Product products_generate_report(id, data)





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
api_instance = defectdojo_api_swagger.ProductsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product.
data = defectdojo_api_swagger.Product() # Product | 

try:
    api_response = api_instance.products_generate_report(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_list**
> InlineResponse20012 products_list(id=id, name=name, prod_type=prod_type, created=created, authorized_users=authorized_users, limit=limit, offset=offset)





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
api_instance = defectdojo_api_swagger.ProductsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 8.14 # float |  (optional)
name = 'name_example' # str |  (optional)
prod_type = 'prod_type_example' # str |  (optional)
created = 'created_example' # str |  (optional)
authorized_users = 'authorized_users_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.products_list(id=id, name=name, prod_type=prod_type, created=created, authorized_users=authorized_users, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **prod_type** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **authorized_users** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_partial_update**
> Product products_partial_update(id, data)





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
api_instance = defectdojo_api_swagger.ProductsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product.
data = defectdojo_api_swagger.Product() # Product | 

try:
    api_response = api_instance.products_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_read**
> Product products_read(id)





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
api_instance = defectdojo_api_swagger.ProductsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product.

try:
    api_response = api_instance.products_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update**
> Product products_update(id, data)





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
api_instance = defectdojo_api_swagger.ProductsApi(defectdojo_api_swagger.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product.
data = defectdojo_api_swagger.Product() # Product | 

try:
    api_response = api_instance.products_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product. | 
 **data** | [**Product**](Product.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

