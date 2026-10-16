# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from workspaces.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from workspaces.model.biomodels_repository_resource import BiomodelsRepositoryResource
from workspaces.model.dandi_repository_resource import DandiRepositoryResource
from workspaces.model.dandi_upload_part import DandiUploadPart
from workspaces.model.dandi_upload_urls_request import DandiUploadUrlsRequest
from workspaces.model.dandi_upload_urls_response import DandiUploadUrlsResponse
from workspaces.model.dandi_uploaded_part import DandiUploadedPart
from workspaces.model.dandi_validate_upload_request import DandiValidateUploadRequest
from workspaces.model.dandi_validate_upload_response import DandiValidateUploadResponse
from workspaces.model.download_resource import DownloadResource
from workspaces.model.figshare_repository_resource import FigshareRepositoryResource
from workspaces.model.git_repository_resource import GITRepositoryResource
from workspaces.model.git_repository_resource_all_of import GITRepositoryResourceAllOf
from workspaces.model.inline_object import InlineObject
from workspaces.model.inline_response200 import InlineResponse200
from workspaces.model.inline_response2001 import InlineResponse2001
from workspaces.model.inline_response2002 import InlineResponse2002
from workspaces.model.inline_response2003 import InlineResponse2003
from workspaces.model.inline_response2004 import InlineResponse2004
from workspaces.model.osb_repository import OSBRepository
from workspaces.model.osb_repository_all_of import OSBRepositoryAllOf
from workspaces.model.osb_repository_base import OSBRepositoryBase
from workspaces.model.osb_repository_entity import OSBRepositoryEntity
from workspaces.model.pagination import Pagination
from workspaces.model.repository_content_type import RepositoryContentType
from workspaces.model.repository_info import RepositoryInfo
from workspaces.model.repository_resource import RepositoryResource
from workspaces.model.repository_resource_base import RepositoryResourceBase
from workspaces.model.repository_resource_base_all_of import RepositoryResourceBaseAllOf
from workspaces.model.repository_resource_node import RepositoryResourceNode
from workspaces.model.repository_type import RepositoryType
from workspaces.model.resource_base import ResourceBase
from workspaces.model.resource_origin import ResourceOrigin
from workspaces.model.resource_status import ResourceStatus
from workspaces.model.resource_type import ResourceType
from workspaces.model.tag import Tag
from workspaces.model.user import User
from workspaces.model.valid import Valid
from workspaces.model.volume_storage import VolumeStorage
from workspaces.model.workspace import Workspace
from workspaces.model.workspace_all_of import WorkspaceAllOf
from workspaces.model.workspace_base import WorkspaceBase
from workspaces.model.workspace_collaborator import WorkspaceCollaborator
from workspaces.model.workspace_entity import WorkspaceEntity
from workspaces.model.workspace_entity_all_of import WorkspaceEntityAllOf
from workspaces.model.workspace_image import WorkspaceImage
from workspaces.model.workspace_resource import WorkspaceResource
from workspaces.model.workspace_resource_all_of import WorkspaceResourceAllOf
from workspaces.model.workspace_resource_base import WorkspaceResourceBase
from workspaces.model.workspace_resource_entity import WorkspaceResourceEntity
from workspaces.model.workspace_resource_entity_all_of import WorkspaceResourceEntityAllOf
from workspaces.model.workspace_run_repo import WorkspaceRunRepo
from workspaces.model.workspace_run_request import WorkspaceRunRequest
from workspaces.model.workspace_run_response import WorkspaceRunResponse
from workspaces.model.workspace_run_results import WorkspaceRunResults
from workspaces.model.workspace_run_setup import WorkspaceRunSetup
