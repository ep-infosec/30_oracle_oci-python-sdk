# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDirectoryObject(object):
    """
    Directory object details, used to define either import or export directory objects in Data Pump Settings.
    Import directory is required for Non-Autonomous target connections. If specified for an autonomous target, it will show an error.
    Export directory will error if there are database link details specified.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDirectoryObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateDirectoryObject.
        :type name: str

        :param path:
            The value to assign to the path property of this CreateDirectoryObject.
        :type path: str

        """
        self.swagger_types = {
            'name': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'path': 'path'
        }

        self._name = None
        self._path = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateDirectoryObject.
        Name of directory object in database


        :return: The name of this CreateDirectoryObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDirectoryObject.
        Name of directory object in database


        :param name: The name of this CreateDirectoryObject.
        :type: str
        """
        self._name = name

    @property
    def path(self):
        """
        **[Required]** Gets the path of this CreateDirectoryObject.
        Absolute path of directory on database server


        :return: The path of this CreateDirectoryObject.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this CreateDirectoryObject.
        Absolute path of directory on database server


        :param path: The path of this CreateDirectoryObject.
        :type: str
        """
        self._path = path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other