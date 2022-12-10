# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExcludedObjectSummary(object):
    """
    Excluded object summary line.
    """

    #: A constant which can be used with the reason_category property of a ExcludedObjectSummary.
    #: This constant has a value of "ORACLE_MAINTAINED"
    REASON_CATEGORY_ORACLE_MAINTAINED = "ORACLE_MAINTAINED"

    #: A constant which can be used with the reason_category property of a ExcludedObjectSummary.
    #: This constant has a value of "GG_UNSUPPORTED"
    REASON_CATEGORY_GG_UNSUPPORTED = "GG_UNSUPPORTED"

    #: A constant which can be used with the reason_category property of a ExcludedObjectSummary.
    #: This constant has a value of "USER_EXCLUDED"
    REASON_CATEGORY_USER_EXCLUDED = "USER_EXCLUDED"

    #: A constant which can be used with the reason_category property of a ExcludedObjectSummary.
    #: This constant has a value of "MANDATORY_EXCLUDED"
    REASON_CATEGORY_MANDATORY_EXCLUDED = "MANDATORY_EXCLUDED"

    #: A constant which can be used with the reason_category property of a ExcludedObjectSummary.
    #: This constant has a value of "USER_EXCLUDED_TYPE"
    REASON_CATEGORY_USER_EXCLUDED_TYPE = "USER_EXCLUDED_TYPE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExcludedObjectSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param owner:
            The value to assign to the owner property of this ExcludedObjectSummary.
        :type owner: str

        :param object:
            The value to assign to the object property of this ExcludedObjectSummary.
        :type object: str

        :param type:
            The value to assign to the type property of this ExcludedObjectSummary.
        :type type: str

        :param reason_category:
            The value to assign to the reason_category property of this ExcludedObjectSummary.
            Allowed values for this property are: "ORACLE_MAINTAINED", "GG_UNSUPPORTED", "USER_EXCLUDED", "MANDATORY_EXCLUDED", "USER_EXCLUDED_TYPE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reason_category: str

        :param source_rule:
            The value to assign to the source_rule property of this ExcludedObjectSummary.
        :type source_rule: str

        """
        self.swagger_types = {
            'owner': 'str',
            'object': 'str',
            'type': 'str',
            'reason_category': 'str',
            'source_rule': 'str'
        }

        self.attribute_map = {
            'owner': 'owner',
            'object': 'object',
            'type': 'type',
            'reason_category': 'reasonCategory',
            'source_rule': 'sourceRule'
        }

        self._owner = None
        self._object = None
        self._type = None
        self._reason_category = None
        self._source_rule = None

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this ExcludedObjectSummary.
        Database object owner.


        :return: The owner of this ExcludedObjectSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this ExcludedObjectSummary.
        Database object owner.


        :param owner: The owner of this ExcludedObjectSummary.
        :type: str
        """
        self._owner = owner

    @property
    def object(self):
        """
        **[Required]** Gets the object of this ExcludedObjectSummary.
        Database object name.


        :return: The object of this ExcludedObjectSummary.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this ExcludedObjectSummary.
        Database object name.


        :param object: The object of this ExcludedObjectSummary.
        :type: str
        """
        self._object = object

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ExcludedObjectSummary.
        Database object type.


        :return: The type of this ExcludedObjectSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ExcludedObjectSummary.
        Database object type.


        :param type: The type of this ExcludedObjectSummary.
        :type: str
        """
        self._type = type

    @property
    def reason_category(self):
        """
        **[Required]** Gets the reason_category of this ExcludedObjectSummary.
        Reason category for object exclusion.

        Allowed values for this property are: "ORACLE_MAINTAINED", "GG_UNSUPPORTED", "USER_EXCLUDED", "MANDATORY_EXCLUDED", "USER_EXCLUDED_TYPE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reason_category of this ExcludedObjectSummary.
        :rtype: str
        """
        return self._reason_category

    @reason_category.setter
    def reason_category(self, reason_category):
        """
        Sets the reason_category of this ExcludedObjectSummary.
        Reason category for object exclusion.


        :param reason_category: The reason_category of this ExcludedObjectSummary.
        :type: str
        """
        allowed_values = ["ORACLE_MAINTAINED", "GG_UNSUPPORTED", "USER_EXCLUDED", "MANDATORY_EXCLUDED", "USER_EXCLUDED_TYPE"]
        if not value_allowed_none_or_none_sentinel(reason_category, allowed_values):
            reason_category = 'UNKNOWN_ENUM_VALUE'
        self._reason_category = reason_category

    @property
    def source_rule(self):
        """
        Gets the source_rule of this ExcludedObjectSummary.
        Reason for exclusion.


        :return: The source_rule of this ExcludedObjectSummary.
        :rtype: str
        """
        return self._source_rule

    @source_rule.setter
    def source_rule(self, source_rule):
        """
        Sets the source_rule of this ExcludedObjectSummary.
        Reason for exclusion.


        :param source_rule: The source_rule of this ExcludedObjectSummary.
        :type: str
        """
        self._source_rule = source_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
