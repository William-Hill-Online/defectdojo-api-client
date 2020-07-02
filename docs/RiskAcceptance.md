# RiskAcceptance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** | Descriptive name which in the future may also be used to group risk acceptances together across engagements and products | 
**path** | **str** |  | [optional] [readonly] 
**accepted_by** | **str** | The entity or person that accepts the risk. | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**compensating_control** | **str** | If a compensating control exists to mitigate the finding or reduce risk, then list the compensating control(s). | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**updated** | **datetime** |  | [optional] [readonly] 
**owner** | **int** | Only the owner and staff users can edit the risk acceptance. | 
**accepted_findings** | **list[int]** |  | 
**notes** | **list[int]** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


