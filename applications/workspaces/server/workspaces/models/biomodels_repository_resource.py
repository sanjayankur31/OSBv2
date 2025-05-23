# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces.models.repository_resource_base import RepositoryResourceBase
from workspaces import util

from workspaces.models.repository_resource_base import RepositoryResourceBase  # noqa: E501

class BiomodelsRepositoryResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, path=None, osbrepository_id=None, size=None, timestamp_modified=None, ref=None, sha=None):  # noqa: E501
        """BiomodelsRepositoryResource - a model defined in OpenAPI

        :param name: The name of this BiomodelsRepositoryResource.  # noqa: E501
        :type name: str
        :param path: The path of this BiomodelsRepositoryResource.  # noqa: E501
        :type path: str
        :param osbrepository_id: The osbrepository_id of this BiomodelsRepositoryResource.  # noqa: E501
        :type osbrepository_id: int
        :param size: The size of this BiomodelsRepositoryResource.  # noqa: E501
        :type size: int
        :param timestamp_modified: The timestamp_modified of this BiomodelsRepositoryResource.  # noqa: E501
        :type timestamp_modified: datetime
        :param ref: The ref of this BiomodelsRepositoryResource.  # noqa: E501
        :type ref: str
        :param sha: The sha of this BiomodelsRepositoryResource.  # noqa: E501
        :type sha: str
        """
        self.openapi_types = {
            'name': str,
            'path': str,
            'osbrepository_id': int,
            'size': int,
            'timestamp_modified': datetime,
            'ref': str,
            'sha': str
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'osbrepository_id': 'osbrepository_id',
            'size': 'size',
            'timestamp_modified': 'timestamp_modified',
            'ref': 'ref',
            'sha': 'sha'
        }

        self._name = name
        self._path = path
        self._osbrepository_id = osbrepository_id
        self._size = size
        self._timestamp_modified = timestamp_modified
        self._ref = ref
        self._sha = sha

    @classmethod
    def from_dict(cls, dikt) -> 'BiomodelsRepositoryResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BiomodelsRepositoryResource of this BiomodelsRepositoryResource.  # noqa: E501
        :rtype: BiomodelsRepositoryResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this BiomodelsRepositoryResource.

        file name  # noqa: E501

        :return: The name of this BiomodelsRepositoryResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BiomodelsRepositoryResource.

        file name  # noqa: E501

        :param name: The name of this BiomodelsRepositoryResource.
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this BiomodelsRepositoryResource.

        Download URL of the Resource  # noqa: E501

        :return: The path of this BiomodelsRepositoryResource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this BiomodelsRepositoryResource.

        Download URL of the Resource  # noqa: E501

        :param path: The path of this BiomodelsRepositoryResource.
        :type path: str
        """

        self._path = path

    @property
    def osbrepository_id(self):
        """Gets the osbrepository_id of this BiomodelsRepositoryResource.

        OSB Repository id  # noqa: E501

        :return: The osbrepository_id of this BiomodelsRepositoryResource.
        :rtype: int
        """
        return self._osbrepository_id

    @osbrepository_id.setter
    def osbrepository_id(self, osbrepository_id):
        """Sets the osbrepository_id of this BiomodelsRepositoryResource.

        OSB Repository id  # noqa: E501

        :param osbrepository_id: The osbrepository_id of this BiomodelsRepositoryResource.
        :type osbrepository_id: int
        """

        self._osbrepository_id = osbrepository_id

    @property
    def size(self):
        """Gets the size of this BiomodelsRepositoryResource.

        File size in bytes of the RepositoryResource  # noqa: E501

        :return: The size of this BiomodelsRepositoryResource.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BiomodelsRepositoryResource.

        File size in bytes of the RepositoryResource  # noqa: E501

        :param size: The size of this BiomodelsRepositoryResource.
        :type size: int
        """

        self._size = size

    @property
    def timestamp_modified(self):
        """Gets the timestamp_modified of this BiomodelsRepositoryResource.

        Date/time the ReposityResource is last modified  # noqa: E501

        :return: The timestamp_modified of this BiomodelsRepositoryResource.
        :rtype: datetime
        """
        return self._timestamp_modified

    @timestamp_modified.setter
    def timestamp_modified(self, timestamp_modified):
        """Sets the timestamp_modified of this BiomodelsRepositoryResource.

        Date/time the ReposityResource is last modified  # noqa: E501

        :param timestamp_modified: The timestamp_modified of this BiomodelsRepositoryResource.
        :type timestamp_modified: datetime
        """

        self._timestamp_modified = timestamp_modified

    @property
    def ref(self):
        """Gets the ref of this BiomodelsRepositoryResource.

        The GIT ref  # noqa: E501

        :return: The ref of this BiomodelsRepositoryResource.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this BiomodelsRepositoryResource.

        The GIT ref  # noqa: E501

        :param ref: The ref of this BiomodelsRepositoryResource.
        :type ref: str
        """

        self._ref = ref

    @property
    def sha(self):
        """Gets the sha of this BiomodelsRepositoryResource.

        The GIT sha of the resource  # noqa: E501

        :return: The sha of this BiomodelsRepositoryResource.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this BiomodelsRepositoryResource.

        The GIT sha of the resource  # noqa: E501

        :param sha: The sha of this BiomodelsRepositoryResource.
        :type sha: str
        """

        self._sha = sha
