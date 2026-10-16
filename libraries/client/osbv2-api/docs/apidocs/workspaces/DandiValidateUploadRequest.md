# DandiValidateUploadRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** | The DANDI deployment, by its dandi-cli name. | 
**username** | **str** | Keycloak user whose DANDI_API_KEY attribute signs the upload; the key must belong to that deployment. | 
**dandiset_id** | **str** |  | 
**path** | **str** | The path get_upload_urls returned. | 
**upload_id** | **str** | Omitted when get_upload_urls returned a blob_id (nothing was uploaded). | [optional] 
**parts** | [**[DandiUploadedPart]**](DandiUploadedPart.md) | Omitted when get_upload_urls returned a blob_id. | [optional] 
**blob_id** | **str** | Echoed from get_upload_urls; when present, complete/validate are skipped. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


