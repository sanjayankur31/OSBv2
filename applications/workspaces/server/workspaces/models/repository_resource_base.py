# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces.models.repository_resource_base_all_of import RepositoryResourceBaseAllOf
from workspaces.models.resource_base import ResourceBase
from workspaces import util

from workspaces.models.repository_resource_base_all_of import RepositoryResourceBaseAllOf  # noqa: E501
from workspaces.models.resource_base import ResourceBase  # noqa: E501

class RepositoryResourceBase(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, path=None, osbrepository_id=None):  # noqa: E501
        """RepositoryResourceBase - a model defined in OpenAPI

        :param name: The name of this RepositoryResourceBase.  # noqa: E501
        :type name: str
        :param path: The path of this RepositoryResourceBase.  # noqa: E501
        :type path: str
        :param osbrepository_id: The osbrepository_id of this RepositoryResourceBase.  # noqa: E501
        :type osbrepository_id: int
        """
        self.openapi_types = {
            'name': str,
            'path': str,
            'osbrepository_id': int
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path',
            'osbrepository_id': 'osbrepository_id'
        }

        self._name = name
        self._path = path
        self._osbrepository_id = osbrepository_id

    @classmethod
    def from_dict(cls, dikt) -> 'RepositoryResourceBase':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RepositoryResourceBase of this RepositoryResourceBase.  # noqa: E501
        :rtype: RepositoryResourceBase
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this RepositoryResourceBase.

        file name  # noqa: E501

        :return: The name of this RepositoryResourceBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepositoryResourceBase.

        file name  # noqa: E501

        :param name: The name of this RepositoryResourceBase.
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this RepositoryResourceBase.

        Download URL of the Resource  # noqa: E501

        :return: The path of this RepositoryResourceBase.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RepositoryResourceBase.

        Download URL of the Resource  # noqa: E501

        :param path: The path of this RepositoryResourceBase.
        :type path: str
        """

        self._path = path

    @property
    def osbrepository_id(self):
        """Gets the osbrepository_id of this RepositoryResourceBase.

        OSB Repository id  # noqa: E501

        :return: The osbrepository_id of this RepositoryResourceBase.
        :rtype: int
        """
        return self._osbrepository_id

    @osbrepository_id.setter
    def osbrepository_id(self, osbrepository_id):
        """Sets the osbrepository_id of this RepositoryResourceBase.

        OSB Repository id  # noqa: E501

        :param osbrepository_id: The osbrepository_id of this RepositoryResourceBase.
        :type osbrepository_id: int
        """

        self._osbrepository_id = osbrepository_id
