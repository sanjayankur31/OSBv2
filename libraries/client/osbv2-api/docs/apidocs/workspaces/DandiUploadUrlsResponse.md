# DandiUploadUrlsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dandiset_id** | **str** |  | 
**path** | **str** | Asset path, built by OSB from the caller&#39;s id. | 
**parts** | [**[DandiUploadPart]**](DandiUploadPart.md) |  | 
**upload_id** | **str** | Absent when the deployment already held this content. | [optional] 
**blob_id** | **str** | Set only when the deployment already held this content (parts is then empty). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


