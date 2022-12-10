# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAssetSourceDetails(object):
    """
    Asset source creation request.
    """

    #: A constant which can be used with the type property of a CreateAssetSourceDetails.
    #: This constant has a value of "VMWARE"
    TYPE_VMWARE = "VMWARE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAssetSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_migrations.models.CreateVmWareAssetSourceDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateAssetSourceDetails.
            Allowed values for this property are: "VMWARE"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this CreateAssetSourceDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAssetSourceDetails.
        :type compartment_id: str

        :param environment_id:
            The value to assign to the environment_id property of this CreateAssetSourceDetails.
        :type environment_id: str

        :param inventory_id:
            The value to assign to the inventory_id property of this CreateAssetSourceDetails.
        :type inventory_id: str

        :param assets_compartment_id:
            The value to assign to the assets_compartment_id property of this CreateAssetSourceDetails.
        :type assets_compartment_id: str

        :param discovery_schedule_id:
            The value to assign to the discovery_schedule_id property of this CreateAssetSourceDetails.
        :type discovery_schedule_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAssetSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAssetSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateAssetSourceDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'environment_id': 'str',
            'inventory_id': 'str',
            'assets_compartment_id': 'str',
            'discovery_schedule_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'environment_id': 'environmentId',
            'inventory_id': 'inventoryId',
            'assets_compartment_id': 'assetsCompartmentId',
            'discovery_schedule_id': 'discoveryScheduleId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._type = None
        self._display_name = None
        self._compartment_id = None
        self._environment_id = None
        self._inventory_id = None
        self._assets_compartment_id = None
        self._discovery_schedule_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'VMWARE':
            return 'CreateVmWareAssetSourceDetails'
        else:
            return 'CreateAssetSourceDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateAssetSourceDetails.
        Asset source type.

        Allowed values for this property are: "VMWARE"


        :return: The type of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateAssetSourceDetails.
        Asset source type.


        :param type: The type of this CreateAssetSourceDetails.
        :type: str
        """
        allowed_values = ["VMWARE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAssetSourceDetails.
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
        Avoid entering confidential information. The name is generated by the service if it is not
        explicitly provided.


        :return: The display_name of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAssetSourceDetails.
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
        Avoid entering confidential information. The name is generated by the service if it is not
        explicitly provided.


        :param display_name: The display_name of this CreateAssetSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAssetSourceDetails.
        The `OCID`__ of the compartment for the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAssetSourceDetails.
        The `OCID`__ of the compartment for the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAssetSourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def environment_id(self):
        """
        **[Required]** Gets the environment_id of this CreateAssetSourceDetails.
        The `OCID`__ of the environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The environment_id of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this CreateAssetSourceDetails.
        The `OCID`__ of the environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param environment_id: The environment_id of this CreateAssetSourceDetails.
        :type: str
        """
        self._environment_id = environment_id

    @property
    def inventory_id(self):
        """
        **[Required]** Gets the inventory_id of this CreateAssetSourceDetails.
        The `OCID`__ of the inventory that will contain created assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The inventory_id of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        """
        Sets the inventory_id of this CreateAssetSourceDetails.
        The `OCID`__ of the inventory that will contain created assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param inventory_id: The inventory_id of this CreateAssetSourceDetails.
        :type: str
        """
        self._inventory_id = inventory_id

    @property
    def assets_compartment_id(self):
        """
        **[Required]** Gets the assets_compartment_id of this CreateAssetSourceDetails.
        The `OCID`__ of the compartment that is going to be used to create assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The assets_compartment_id of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._assets_compartment_id

    @assets_compartment_id.setter
    def assets_compartment_id(self, assets_compartment_id):
        """
        Sets the assets_compartment_id of this CreateAssetSourceDetails.
        The `OCID`__ of the compartment that is going to be used to create assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param assets_compartment_id: The assets_compartment_id of this CreateAssetSourceDetails.
        :type: str
        """
        self._assets_compartment_id = assets_compartment_id

    @property
    def discovery_schedule_id(self):
        """
        Gets the discovery_schedule_id of this CreateAssetSourceDetails.
        The `OCID`__ of the discovery schedule that is going to be attached to the created asset.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The discovery_schedule_id of this CreateAssetSourceDetails.
        :rtype: str
        """
        return self._discovery_schedule_id

    @discovery_schedule_id.setter
    def discovery_schedule_id(self, discovery_schedule_id):
        """
        Sets the discovery_schedule_id of this CreateAssetSourceDetails.
        The `OCID`__ of the discovery schedule that is going to be attached to the created asset.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param discovery_schedule_id: The discovery_schedule_id of this CreateAssetSourceDetails.
        :type: str
        """
        self._discovery_schedule_id = discovery_schedule_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAssetSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateAssetSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAssetSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateAssetSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAssetSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateAssetSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAssetSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateAssetSourceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateAssetSourceDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreateAssetSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateAssetSourceDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreateAssetSourceDetails.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
