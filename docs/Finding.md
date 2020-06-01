# Finding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**images** | [**list[FindingImage]**](FindingImage.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**accepted_risks** | [**list[RiskAcceptance]**](RiskAcceptance.md) |  | [optional] 
**push_to_jira** | **bool** |  | [optional] [default to False]
**age** | **int** |  | [optional] 
**sla_days_remaining** | **int** |  | [optional] 
**title** | **str** |  | 
**_date** | **date** |  | [optional] 
**cwe** | **int** |  | [optional] 
**cve** | **str** | CVE or other vulnerability identifier | [optional] 
**url** | **str** |  | [optional] 
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
**thread_id** | **int** |  | [optional] 
**mitigated** | **datetime** |  | [optional] 
**numerical_severity** | **str** |  | 
**last_reviewed** | **datetime** |  | [optional] 
**line_number** | **str** |  | [optional] 
**sourcefilepath** | **str** |  | [optional] 
**sourcefile** | **str** |  | [optional] 
**param** | **str** |  | [optional] 
**payload** | **str** |  | [optional] 
**hash_code** | **str** |  | [optional] 
**line** | **int** | Line number. For SAST, when source (start of the attack vector) and sink (end of the attack vector) information are available, put sink information here | [optional] 
**file_path** | **str** | File name with path. For SAST, when source (start of the attack vector) and sink (end of the attack vector) information are available, put sink information here | [optional] 
**component_name** | **str** | Name of the component containing the finding.  | [optional] 
**component_version** | **str** | Version of the component. | [optional] 
**static_finding** | **bool** |  | [optional] 
**dynamic_finding** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**jira_creation** | **datetime** |  | [optional] 
**jira_change** | **datetime** |  | [optional] 
**scanner_confidence** | **int** | Confidence level of vulnerability which is supplied by the scannner. | [optional] 
**unique_id_from_tool** | **str** | Vulnerability technical id from the source tool. Allows to track unique vulnerabilities | [optional] 
**sast_source_object** | **str** | Source object (variable, function...) of the attack vector | [optional] 
**sast_sink_object** | **str** | Sink object (variable, function...) of the attack vector | [optional] 
**sast_source_line** | **int** | Source line number of the attack vector | [optional] 
**sast_source_file_path** | **str** | Source filepath of the attack vector | [optional] 
**nb_occurences** | **int** | Number of occurences in the source tool when several vulnerabilites were found and aggregated by the scanner | [optional] 
**test** | **int** |  | [optional] 
**duplicate_finding** | **int** |  | [optional] 
**review_requested_by** | **int** |  | [optional] 
**defect_review_requested_by** | **int** |  | [optional] 
**mitigated_by** | **int** |  | [optional] 
**reporter** | **int** |  | [optional] 
**last_reviewed_by** | **int** |  | [optional] 
**sonarqube_issue** | **int** | SonarQube issue | [optional] 
**endpoints** | **list[int]** |  | [optional] 
**reviewers** | **list[int]** |  | [optional] 
**notes** | [**list[Note]**](Note.md) |  | [optional] 
**found_by** | **list[int]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


