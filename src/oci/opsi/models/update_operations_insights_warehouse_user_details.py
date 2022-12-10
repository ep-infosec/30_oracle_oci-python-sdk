# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOperationsInsightsWarehouseUserDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOperationsInsightsWarehouseUserDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_password:
            The value to assign to the connection_password property of this UpdateOperationsInsightsWarehouseUserDetails.
        :type connection_password: str

        :param is_awr_data_access:
            The value to assign to the is_awr_data_access property of this UpdateOperationsInsightsWarehouseUserDetails.
        :type is_awr_data_access: bool

        :param is_em_data_access:
            The value to assign to the is_em_data_access property of this UpdateOperationsInsightsWarehouseUserDetails.
        :type is_em_data_access: bool

        :param is_opsi_data_access:
            The value to assign to the is_opsi_data_access property of this UpdateOperationsInsightsWarehouseUserDetails.
        :type is_opsi_data_access: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOperationsInsightsWarehouseUserDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOperationsInsightsWarehouseUserDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'connection_password': 'str',
            'is_awr_data_access': 'bool',
            'is_em_data_access': 'bool',
            'is_opsi_data_access': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'connection_password': 'connectionPassword',
            'is_awr_data_access': 'isAwrDataAccess',
            'is_em_data_access': 'isEmDataAccess',
            'is_opsi_data_access': 'isOpsiDataAccess',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._connection_password = None
        self._is_awr_data_access = None
        self._is_em_data_access = None
        self._is_opsi_data_access = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def connection_password(self):
        """
        Gets the connection_password of this UpdateOperationsInsightsWarehouseUserDetails.
        User provided connection password for the AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.


        :return: The connection_password of this UpdateOperationsInsightsWarehouseUserDetails.
        :rtype: str
        """
        return self._connection_password

    @connection_password.setter
    def connection_password(self, connection_password):
        """
        Sets the connection_password of this UpdateOperationsInsightsWarehouseUserDetails.
        User provided connection password for the AWR Data,  Enterprise Manager Data and Operations Insights OPSI Hub.


        :param connection_password: The connection_password of this UpdateOperationsInsightsWarehouseUserDetails.
        :type: str
        """
        self._connection_password = connection_password

    @property
    def is_awr_data_access(self):
        """
        Gets the is_awr_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to AWR data.


        :return: The is_awr_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        :rtype: bool
        """
        return self._is_awr_data_access

    @is_awr_data_access.setter
    def is_awr_data_access(self, is_awr_data_access):
        """
        Sets the is_awr_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to AWR data.


        :param is_awr_data_access: The is_awr_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        :type: bool
        """
        self._is_awr_data_access = is_awr_data_access

    @property
    def is_em_data_access(self):
        """
        Gets the is_em_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to EM data.


        :return: The is_em_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        :rtype: bool
        """
        return self._is_em_data_access

    @is_em_data_access.setter
    def is_em_data_access(self, is_em_data_access):
        """
        Sets the is_em_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to EM data.


        :param is_em_data_access: The is_em_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        :type: bool
        """
        self._is_em_data_access = is_em_data_access

    @property
    def is_opsi_data_access(self):
        """
        Gets the is_opsi_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to OPSI data.


        :return: The is_opsi_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        :rtype: bool
        """
        return self._is_opsi_data_access

    @is_opsi_data_access.setter
    def is_opsi_data_access(self, is_opsi_data_access):
        """
        Sets the is_opsi_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        Indicate whether user has access to OPSI data.


        :param is_opsi_data_access: The is_opsi_data_access of this UpdateOperationsInsightsWarehouseUserDetails.
        :type: bool
        """
        self._is_opsi_data_access = is_opsi_data_access

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOperationsInsightsWarehouseUserDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
