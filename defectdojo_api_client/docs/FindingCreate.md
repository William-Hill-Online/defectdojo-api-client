# FindingCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**notes** | **list[int]** |  | [optional] [readonly] 
**test** | **int** |  | 
**thread_id** | **int** |  | [optional] 
**found_by** | **list[int]** |  | 
**url** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**push_to_jira** | **bool** |  | [optional] [default to False]
**title** | **str** |  | 
**date** | **date** |  | [optional] 
**cwe** | **int** |  | [optional] 
**cve** | **str** | CVE or other vulnerability identifier | [optional] 
**severity** | **str** | The severity level of this flaw (Critical, High, Medium, Low, Informational) | 
**description** | **str** |  | 
**mitigation** | **str** |  | 
**impact** | **str** |  | 
**steps_to_reproduce** | **str** |  | [optional] 
**severity_justification** | **str** |  | [optional] 
**references** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**false_p** | **bool** |  | [optional] 
**duplicate** | **bool** |  | [optional] 
**out_of_scope** | **bool** |  | [optional] 
**under_review** | **bool** |  | [optional] 
**under_defect_review** | **bool** |  | [optional] 
**is_mitigated** | **bool** |  | [optional] 
**mitigated** | **datetime** |  | [optional] [readonly] 
**numerical_severity** | **str** |  | 
**last_reviewed** | **datetime** |  | [optional] [readonly] 
**line_number** | **str** |  | [optional] [readonly] 
**sourcefilepath** | **str** |  | [optional] [readonly] 
**sourcefile** | **str** |  | [optional] [readonly] 
**param** | **str** |  | [optional] [readonly] 
**payload** | **str** |  | [optional] [readonly] 
**hash_code** | **str** |  | [optional] [readonly] 
**line** | **int** | Line number. For SAST, when source (start of the attack vector) and sink (end of the attack vector) information are available, put sink information here | [optional] 
**file_path** | **str** | File name with path. For SAST, when source (start of the attack vector) and sink (end of the attack vector) information are available, put sink information here | [optional] 
**component_name** | **str** | Name of the component containing the finding.  | [optional] 
**component_version** | **str** | Version of the component. | [optional] 
**static_finding** | **bool** |  | [optional] 
**dynamic_finding** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**jira_creation** | **datetime** |  | [optional] 
**jira_change** | **datetime** |  | [optional] 
**scanner_confidence** | **int** | Confidence level of vulnerability which is supplied by the scannner. | [optional] [readonly] 
**unique_id_from_tool** | **str** | Vulnerability technical id from the source tool. Allows to track unique vulnerabilities | [optional] 
**sast_source_object** | **str** | Source object (variable, function...) of the attack vector | [optional] 
**sast_sink_object** | **str** | Sink object (variable, function...) of the attack vector | [optional] 
**sast_source_line** | **int** | Source line number of the attack vector | [optional] 
**sast_source_file_path** | **str** | Source filepath of the attack vector | [optional] 
**nb_occurences** | **int** | Number of occurences in the source tool when several vulnerabilites were found and aggregated by the scanner | [optional] 
**duplicate_finding** | **int** |  | [optional] [readonly] 
**review_requested_by** | **int** |  | [optional] 
**defect_review_requested_by** | **int** |  | [optional] 
**mitigated_by** | **int** |  | [optional] [readonly] 
**reporter** | **int** |  | [optional] [readonly] 
**last_reviewed_by** | **int** |  | [optional] [readonly] 
**sonarqube_issue** | **int** | SonarQube issue | [optional] 
**endpoints** | **list[int]** |  | [optional] 
**reviewers** | **list[int]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


