# DandiUploadUrlsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** | The DANDI deployment, by its dandi-cli name. | 
**username** | **str** | Keycloak user whose DANDI_API_KEY attribute signs the upload; the key must belong to that deployment. | 
**dandiset_id** | **str** | The dandiset to upload into, chosen by the client. | 
**filename** | **str** |  | 
**size** | **int** |  | 
**dandi_etag** | **str** | S3-multipart digest in DANDI&#39;s format (32 hex chars, a dash, the part count), computed by the client since the bytes never reach this server. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


