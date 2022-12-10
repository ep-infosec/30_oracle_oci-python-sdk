# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GrantSummary(object):
    """
    The summary of user grants.
    """

    #: A constant which can be used with the privilege_type property of a GrantSummary.
    #: This constant has a value of "SYSTEM_PRIVILEGE"
    PRIVILEGE_TYPE_SYSTEM_PRIVILEGE = "SYSTEM_PRIVILEGE"

    #: A constant which can be used with the privilege_type property of a GrantSummary.
    #: This constant has a value of "OBJECT_PRIVILEGE"
    PRIVILEGE_TYPE_OBJECT_PRIVILEGE = "OBJECT_PRIVILEGE"

    #: A constant which can be used with the privilege_type property of a GrantSummary.
    #: This constant has a value of "ADMIN_PRIVILEGE"
    PRIVILEGE_TYPE_ADMIN_PRIVILEGE = "ADMIN_PRIVILEGE"

    #: A constant which can be used with the privilege_type property of a GrantSummary.
    #: This constant has a value of "ROLE"
    PRIVILEGE_TYPE_ROLE = "ROLE"

    #: A constant which can be used with the privilege_category property of a GrantSummary.
    #: This constant has a value of "CRITICAL"
    PRIVILEGE_CATEGORY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the privilege_category property of a GrantSummary.
    #: This constant has a value of "HIGH"
    PRIVILEGE_CATEGORY_HIGH = "HIGH"

    #: A constant which can be used with the privilege_category property of a GrantSummary.
    #: This constant has a value of "MEDIUM"
    PRIVILEGE_CATEGORY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the privilege_category property of a GrantSummary.
    #: This constant has a value of "LOW"
    PRIVILEGE_CATEGORY_LOW = "LOW"

    def __init__(self, **kwargs):
        """
        Initializes a new GrantSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this GrantSummary.
        :type key: str

        :param grant_name:
            The value to assign to the grant_name property of this GrantSummary.
        :type grant_name: str

        :param privilege_type:
            The value to assign to the privilege_type property of this GrantSummary.
            Allowed values for this property are: "SYSTEM_PRIVILEGE", "OBJECT_PRIVILEGE", "ADMIN_PRIVILEGE", "ROLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type privilege_type: str

        :param privilege_category:
            The value to assign to the privilege_category property of this GrantSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type privilege_category: str

        :param depth_level:
            The value to assign to the depth_level property of this GrantSummary.
        :type depth_level: int

        """
        self.swagger_types = {
            'key': 'str',
            'grant_name': 'str',
            'privilege_type': 'str',
            'privilege_category': 'str',
            'depth_level': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'grant_name': 'grantName',
            'privilege_type': 'privilegeType',
            'privilege_category': 'privilegeCategory',
            'depth_level': 'depthLevel'
        }

        self._key = None
        self._grant_name = None
        self._privilege_type = None
        self._privilege_category = None
        self._depth_level = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this GrantSummary.
        The unique key of a user grant.


        :return: The key of this GrantSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this GrantSummary.
        The unique key of a user grant.


        :param key: The key of this GrantSummary.
        :type: str
        """
        self._key = key

    @property
    def grant_name(self):
        """
        Gets the grant_name of this GrantSummary.
        The name of a user grant.


        :return: The grant_name of this GrantSummary.
        :rtype: str
        """
        return self._grant_name

    @grant_name.setter
    def grant_name(self, grant_name):
        """
        Sets the grant_name of this GrantSummary.
        The name of a user grant.


        :param grant_name: The grant_name of this GrantSummary.
        :type: str
        """
        self._grant_name = grant_name

    @property
    def privilege_type(self):
        """
        Gets the privilege_type of this GrantSummary.
        The type of a user grant.

        Allowed values for this property are: "SYSTEM_PRIVILEGE", "OBJECT_PRIVILEGE", "ADMIN_PRIVILEGE", "ROLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The privilege_type of this GrantSummary.
        :rtype: str
        """
        return self._privilege_type

    @privilege_type.setter
    def privilege_type(self, privilege_type):
        """
        Sets the privilege_type of this GrantSummary.
        The type of a user grant.


        :param privilege_type: The privilege_type of this GrantSummary.
        :type: str
        """
        allowed_values = ["SYSTEM_PRIVILEGE", "OBJECT_PRIVILEGE", "ADMIN_PRIVILEGE", "ROLE"]
        if not value_allowed_none_or_none_sentinel(privilege_type, allowed_values):
            privilege_type = 'UNKNOWN_ENUM_VALUE'
        self._privilege_type = privilege_type

    @property
    def privilege_category(self):
        """
        Gets the privilege_category of this GrantSummary.
        The privilege category.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The privilege_category of this GrantSummary.
        :rtype: str
        """
        return self._privilege_category

    @privilege_category.setter
    def privilege_category(self, privilege_category):
        """
        Sets the privilege_category of this GrantSummary.
        The privilege category.


        :param privilege_category: The privilege_category of this GrantSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if not value_allowed_none_or_none_sentinel(privilege_category, allowed_values):
            privilege_category = 'UNKNOWN_ENUM_VALUE'
        self._privilege_category = privilege_category

    @property
    def depth_level(self):
        """
        Gets the depth_level of this GrantSummary.
        The grant depth level of the indirect grant.
        An indirectly granted role/privilege is granted to the user through another role.
        The depth level indicates how deep a privilege is within the grant hierarchy.


        :return: The depth_level of this GrantSummary.
        :rtype: int
        """
        return self._depth_level

    @depth_level.setter
    def depth_level(self, depth_level):
        """
        Sets the depth_level of this GrantSummary.
        The grant depth level of the indirect grant.
        An indirectly granted role/privilege is granted to the user through another role.
        The depth level indicates how deep a privilege is within the grant hierarchy.


        :param depth_level: The depth_level of this GrantSummary.
        :type: int
        """
        self._depth_level = depth_level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
