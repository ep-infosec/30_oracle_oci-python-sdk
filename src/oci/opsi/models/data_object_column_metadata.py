# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectColumnMetadata(object):
    """
    Metadata of a column in a data object resultset.
    """

    #: A constant which can be used with the category property of a DataObjectColumnMetadata.
    #: This constant has a value of "DIMENSION"
    CATEGORY_DIMENSION = "DIMENSION"

    #: A constant which can be used with the category property of a DataObjectColumnMetadata.
    #: This constant has a value of "METRIC"
    CATEGORY_METRIC = "METRIC"

    #: A constant which can be used with the category property of a DataObjectColumnMetadata.
    #: This constant has a value of "TIME_DIMENSION"
    CATEGORY_TIME_DIMENSION = "TIME_DIMENSION"

    #: A constant which can be used with the data_type_name property of a DataObjectColumnMetadata.
    #: This constant has a value of "NUMBER"
    DATA_TYPE_NAME_NUMBER = "NUMBER"

    #: A constant which can be used with the data_type_name property of a DataObjectColumnMetadata.
    #: This constant has a value of "TIMESTAMP"
    DATA_TYPE_NAME_TIMESTAMP = "TIMESTAMP"

    #: A constant which can be used with the data_type_name property of a DataObjectColumnMetadata.
    #: This constant has a value of "VARCHAR2"
    DATA_TYPE_NAME_VARCHAR2 = "VARCHAR2"

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectColumnMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DataObjectColumnMetadata.
        :type name: str

        :param category:
            The value to assign to the category property of this DataObjectColumnMetadata.
            Allowed values for this property are: "DIMENSION", "METRIC", "TIME_DIMENSION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        :param data_type_name:
            The value to assign to the data_type_name property of this DataObjectColumnMetadata.
            Allowed values for this property are: "NUMBER", "TIMESTAMP", "VARCHAR2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type_name: str

        :param display_name:
            The value to assign to the display_name property of this DataObjectColumnMetadata.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DataObjectColumnMetadata.
        :type description: str

        :param group_name:
            The value to assign to the group_name property of this DataObjectColumnMetadata.
        :type group_name: str

        :param unit_details:
            The value to assign to the unit_details property of this DataObjectColumnMetadata.
        :type unit_details: oci.opsi.models.DataObjectColumnUnit

        """
        self.swagger_types = {
            'name': 'str',
            'category': 'str',
            'data_type_name': 'str',
            'display_name': 'str',
            'description': 'str',
            'group_name': 'str',
            'unit_details': 'DataObjectColumnUnit'
        }

        self.attribute_map = {
            'name': 'name',
            'category': 'category',
            'data_type_name': 'dataTypeName',
            'display_name': 'displayName',
            'description': 'description',
            'group_name': 'groupName',
            'unit_details': 'unitDetails'
        }

        self._name = None
        self._category = None
        self._data_type_name = None
        self._display_name = None
        self._description = None
        self._group_name = None
        self._unit_details = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DataObjectColumnMetadata.
        Name of the column.


        :return: The name of this DataObjectColumnMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataObjectColumnMetadata.
        Name of the column.


        :param name: The name of this DataObjectColumnMetadata.
        :type: str
        """
        self._name = name

    @property
    def category(self):
        """
        Gets the category of this DataObjectColumnMetadata.
        Category of the column.

        Allowed values for this property are: "DIMENSION", "METRIC", "TIME_DIMENSION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this DataObjectColumnMetadata.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this DataObjectColumnMetadata.
        Category of the column.


        :param category: The category of this DataObjectColumnMetadata.
        :type: str
        """
        allowed_values = ["DIMENSION", "METRIC", "TIME_DIMENSION"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    @property
    def data_type_name(self):
        """
        Gets the data_type_name of this DataObjectColumnMetadata.
        Type of a data object column.

        Allowed values for this property are: "NUMBER", "TIMESTAMP", "VARCHAR2", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type_name of this DataObjectColumnMetadata.
        :rtype: str
        """
        return self._data_type_name

    @data_type_name.setter
    def data_type_name(self, data_type_name):
        """
        Sets the data_type_name of this DataObjectColumnMetadata.
        Type of a data object column.


        :param data_type_name: The data_type_name of this DataObjectColumnMetadata.
        :type: str
        """
        allowed_values = ["NUMBER", "TIMESTAMP", "VARCHAR2"]
        if not value_allowed_none_or_none_sentinel(data_type_name, allowed_values):
            data_type_name = 'UNKNOWN_ENUM_VALUE'
        self._data_type_name = data_type_name

    @property
    def display_name(self):
        """
        Gets the display_name of this DataObjectColumnMetadata.
        Display name of the column.


        :return: The display_name of this DataObjectColumnMetadata.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DataObjectColumnMetadata.
        Display name of the column.


        :param display_name: The display_name of this DataObjectColumnMetadata.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DataObjectColumnMetadata.
        Description of the column.


        :return: The description of this DataObjectColumnMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataObjectColumnMetadata.
        Description of the column.


        :param description: The description of this DataObjectColumnMetadata.
        :type: str
        """
        self._description = description

    @property
    def group_name(self):
        """
        Gets the group_name of this DataObjectColumnMetadata.
        Group name of the column.


        :return: The group_name of this DataObjectColumnMetadata.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this DataObjectColumnMetadata.
        Group name of the column.


        :param group_name: The group_name of this DataObjectColumnMetadata.
        :type: str
        """
        self._group_name = group_name

    @property
    def unit_details(self):
        """
        Gets the unit_details of this DataObjectColumnMetadata.

        :return: The unit_details of this DataObjectColumnMetadata.
        :rtype: oci.opsi.models.DataObjectColumnUnit
        """
        return self._unit_details

    @unit_details.setter
    def unit_details(self, unit_details):
        """
        Sets the unit_details of this DataObjectColumnMetadata.

        :param unit_details: The unit_details of this DataObjectColumnMetadata.
        :type: oci.opsi.models.DataObjectColumnUnit
        """
        self._unit_details = unit_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
