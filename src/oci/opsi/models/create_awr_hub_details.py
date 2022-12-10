# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAwrHubDetails(object):
    """
    The information about Hub to be analyzed. Input compartmentId MUST be the root compartment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAwrHubDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operations_insights_warehouse_id:
            The value to assign to the operations_insights_warehouse_id property of this CreateAwrHubDetails.
        :type operations_insights_warehouse_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAwrHubDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateAwrHubDetails.
        :type display_name: str

        :param object_storage_bucket_name:
            The value to assign to the object_storage_bucket_name property of this CreateAwrHubDetails.
        :type object_storage_bucket_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAwrHubDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAwrHubDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'operations_insights_warehouse_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'object_storage_bucket_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'operations_insights_warehouse_id': 'operationsInsightsWarehouseId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'object_storage_bucket_name': 'objectStorageBucketName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._operations_insights_warehouse_id = None
        self._compartment_id = None
        self._display_name = None
        self._object_storage_bucket_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def operations_insights_warehouse_id(self):
        """
        **[Required]** Gets the operations_insights_warehouse_id of this CreateAwrHubDetails.
        OPSI Warehouse OCID


        :return: The operations_insights_warehouse_id of this CreateAwrHubDetails.
        :rtype: str
        """
        return self._operations_insights_warehouse_id

    @operations_insights_warehouse_id.setter
    def operations_insights_warehouse_id(self, operations_insights_warehouse_id):
        """
        Sets the operations_insights_warehouse_id of this CreateAwrHubDetails.
        OPSI Warehouse OCID


        :param operations_insights_warehouse_id: The operations_insights_warehouse_id of this CreateAwrHubDetails.
        :type: str
        """
        self._operations_insights_warehouse_id = operations_insights_warehouse_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAwrHubDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAwrHubDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAwrHubDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAwrHubDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAwrHubDetails.
        User-friedly name of AWR Hub that does not have to be unique.


        :return: The display_name of this CreateAwrHubDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAwrHubDetails.
        User-friedly name of AWR Hub that does not have to be unique.


        :param display_name: The display_name of this CreateAwrHubDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def object_storage_bucket_name(self):
        """
        **[Required]** Gets the object_storage_bucket_name of this CreateAwrHubDetails.
        Object Storage Bucket Name


        :return: The object_storage_bucket_name of this CreateAwrHubDetails.
        :rtype: str
        """
        return self._object_storage_bucket_name

    @object_storage_bucket_name.setter
    def object_storage_bucket_name(self, object_storage_bucket_name):
        """
        Sets the object_storage_bucket_name of this CreateAwrHubDetails.
        Object Storage Bucket Name


        :param object_storage_bucket_name: The object_storage_bucket_name of this CreateAwrHubDetails.
        :type: str
        """
        self._object_storage_bucket_name = object_storage_bucket_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAwrHubDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateAwrHubDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAwrHubDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateAwrHubDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAwrHubDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateAwrHubDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAwrHubDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateAwrHubDetails.
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
