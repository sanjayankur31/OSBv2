# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from workspaces.models.base_model_ import Model
from workspaces.models.repository_resource_base import RepositoryResourceBase
from workspaces import util

from workspaces.models.repository_resource_base import RepositoryResourceBase  # noqa: E501

class DandiRepositoryResource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, path=None, osbrepository_id=None):  # noqa: E501
        """DandiRepositoryResource - a model defined in OpenAPI

        :param name: The name of this DandiRepositoryResource.  # noqa: E501
        :type name: str
        :param path: The path of this DandiRepositoryResource.  # noqa: E501
        :type path: str
        :param osbrepository_id: The osbrepository_id of this DandiRepositoryResource.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'DandiRepositoryResource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DandiRepositoryResource of this DandiRepositoryResource.  # noqa: E501
        :rtype: DandiRepositoryResource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this DandiRepositoryResource.

        file name  # noqa: E501

        :return: The name of this DandiRepositoryResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DandiRepositoryResource.

        file name  # noqa: E501

        :param name: The name of this DandiRepositoryResource.
        :type name: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this DandiRepositoryResource.

        Download URL of the Resource  # noqa: E501

        :return: The path of this DandiRepositoryResource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DandiRepositoryResource.

        Download URL of the Resource  # noqa: E501

        :param path: The path of this DandiRepositoryResource.
        :type path: str
        """

        self._path = path

    @property
    def osbrepository_id(self):
        """Gets the osbrepository_id of this DandiRepositoryResource.

        OSB Repository id  # noqa: E501

        :return: The osbrepository_id of this DandiRepositoryResource.
        :rtype: int
        """
        return self._osbrepository_id

    @osbrepository_id.setter
    def osbrepository_id(self, osbrepository_id):
        """Sets the osbrepository_id of this DandiRepositoryResource.

        OSB Repository id  # noqa: E501

        :param osbrepository_id: The osbrepository_id of this DandiRepositoryResource.
        :type osbrepository_id: int
        """

        self._osbrepository_id = osbrepository_id
