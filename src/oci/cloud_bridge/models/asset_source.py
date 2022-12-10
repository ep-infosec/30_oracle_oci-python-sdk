# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssetSource(object):
    """
    Asset source.
    """

    #: A constant which can be used with the type property of a AssetSource.
    #: This constant has a value of "VMWARE"
    TYPE_VMWARE = "VMWARE"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AssetSource.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new AssetSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_bridge.models.VmWareAssetSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AssetSource.
            Allowed values for this property are: "VMWARE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param id:
            The value to assign to the id property of this AssetSource.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AssetSource.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AssetSource.
        :type display_name: str

        :param environment_id:
            The value to assign to the environment_id property of this AssetSource.
        :type environment_id: str

        :param inventory_id:
            The value to assign to the inventory_id property of this AssetSource.
        :type inventory_id: str

        :param assets_compartment_id:
            The value to assign to the assets_compartment_id property of this AssetSource.
        :type assets_compartment_id: str

        :param discovery_schedule_id:
            The value to assign to the discovery_schedule_id property of this AssetSource.
        :type discovery_schedule_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AssetSource.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AssetSource.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this AssetSource.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this AssetSource.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AssetSource.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AssetSource.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this AssetSource.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'environment_id': 'str',
            'inventory_id': 'str',
            'assets_compartment_id': 'str',
            'discovery_schedule_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'environment_id': 'environmentId',
            'inventory_id': 'inventoryId',
            'assets_compartment_id': 'assetsCompartmentId',
            'discovery_schedule_id': 'discoveryScheduleId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._type = None
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._environment_id = None
        self._inventory_id = None
        self._assets_compartment_id = None
        self._discovery_schedule_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
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
            return 'VmWareAssetSource'
        else:
            return 'AssetSource'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AssetSource.
        The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.

        Allowed values for this property are: "VMWARE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AssetSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AssetSource.
        The type of asset source. Indicates external origin of the assets that are read by assigning this asset source.


        :param type: The type of this AssetSource.
        :type: str
        """
        allowed_values = ["VMWARE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssetSource.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AssetSource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssetSource.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AssetSource.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AssetSource.
        The `OCID`__ of the compartment for the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AssetSource.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AssetSource.
        The `OCID`__ of the compartment for the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AssetSource.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AssetSource.
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
        Avoid entering confidential information.


        :return: The display_name of this AssetSource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AssetSource.
        A user-friendly name for the asset source. Does not have to be unique, and it's mutable.
        Avoid entering confidential information.


        :param display_name: The display_name of this AssetSource.
        :type: str
        """
        self._display_name = display_name

    @property
    def environment_id(self):
        """
        **[Required]** Gets the environment_id of this AssetSource.
        The `OCID`__ of the environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The environment_id of this AssetSource.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this AssetSource.
        The `OCID`__ of the environment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param environment_id: The environment_id of this AssetSource.
        :type: str
        """
        self._environment_id = environment_id

    @property
    def inventory_id(self):
        """
        **[Required]** Gets the inventory_id of this AssetSource.
        The `OCID`__ of the inventory that will contain created assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The inventory_id of this AssetSource.
        :rtype: str
        """
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        """
        Sets the inventory_id of this AssetSource.
        The `OCID`__ of the inventory that will contain created assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param inventory_id: The inventory_id of this AssetSource.
        :type: str
        """
        self._inventory_id = inventory_id

    @property
    def assets_compartment_id(self):
        """
        **[Required]** Gets the assets_compartment_id of this AssetSource.
        The `OCID`__ of the compartment that is going to be used to create assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The assets_compartment_id of this AssetSource.
        :rtype: str
        """
        return self._assets_compartment_id

    @assets_compartment_id.setter
    def assets_compartment_id(self, assets_compartment_id):
        """
        Sets the assets_compartment_id of this AssetSource.
        The `OCID`__ of the compartment that is going to be used to create assets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param assets_compartment_id: The assets_compartment_id of this AssetSource.
        :type: str
        """
        self._assets_compartment_id = assets_compartment_id

    @property
    def discovery_schedule_id(self):
        """
        Gets the discovery_schedule_id of this AssetSource.
        The `OCID`__ of an attached discovery schedule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The discovery_schedule_id of this AssetSource.
        :rtype: str
        """
        return self._discovery_schedule_id

    @discovery_schedule_id.setter
    def discovery_schedule_id(self, discovery_schedule_id):
        """
        Sets the discovery_schedule_id of this AssetSource.
        The `OCID`__ of an attached discovery schedule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param discovery_schedule_id: The discovery_schedule_id of this AssetSource.
        :type: str
        """
        self._discovery_schedule_id = discovery_schedule_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AssetSource.
        The current state of the asset source.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AssetSource.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AssetSource.
        The current state of the asset source.


        :param lifecycle_state: The lifecycle_state of this AssetSource.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this AssetSource.
        The detailed state of the asset source.


        :return: The lifecycle_details of this AssetSource.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AssetSource.
        The detailed state of the asset source.


        :param lifecycle_details: The lifecycle_details of this AssetSource.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AssetSource.
        The time when the asset source was created in the RFC3339 format.


        :return: The time_created of this AssetSource.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AssetSource.
        The time when the asset source was created in the RFC3339 format.


        :param time_created: The time_created of this AssetSource.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this AssetSource.
        The point in time that the asset source was last updated in the RFC3339 format.


        :return: The time_updated of this AssetSource.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this AssetSource.
        The point in time that the asset source was last updated in the RFC3339 format.


        :param time_updated: The time_updated of this AssetSource.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AssetSource.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AssetSource.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AssetSource.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AssetSource.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AssetSource.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AssetSource.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AssetSource.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AssetSource.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AssetSource.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this AssetSource.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AssetSource.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this AssetSource.
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
