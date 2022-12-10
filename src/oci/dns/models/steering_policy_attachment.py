# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyAttachment(object):
    """
    An attachment between a steering policy and a domain. An attachment constructs
    DNS responses using its steering policy instead of the records at its defined domain.
    Only records of the policy's covered rtype are blocked at the domain.
    A domain can have a maximum of one attachment covering any given rtype.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicyAttachment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicyAttachment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicyAttachment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyAttachment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param steering_policy_id:
            The value to assign to the steering_policy_id property of this SteeringPolicyAttachment.
        :type steering_policy_id: str

        :param zone_id:
            The value to assign to the zone_id property of this SteeringPolicyAttachment.
        :type zone_id: str

        :param domain_name:
            The value to assign to the domain_name property of this SteeringPolicyAttachment.
        :type domain_name: str

        :param display_name:
            The value to assign to the display_name property of this SteeringPolicyAttachment.
        :type display_name: str

        :param rtypes:
            The value to assign to the rtypes property of this SteeringPolicyAttachment.
        :type rtypes: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this SteeringPolicyAttachment.
        :type compartment_id: str

        :param _self:
            The value to assign to the _self property of this SteeringPolicyAttachment.
        :type _self: str

        :param id:
            The value to assign to the id property of this SteeringPolicyAttachment.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this SteeringPolicyAttachment.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SteeringPolicyAttachment.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'steering_policy_id': 'str',
            'zone_id': 'str',
            'domain_name': 'str',
            'display_name': 'str',
            'rtypes': 'list[str]',
            'compartment_id': 'str',
            '_self': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'steering_policy_id': 'steeringPolicyId',
            'zone_id': 'zoneId',
            'domain_name': 'domainName',
            'display_name': 'displayName',
            'rtypes': 'rtypes',
            'compartment_id': 'compartmentId',
            '_self': 'self',
            'id': 'id',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._steering_policy_id = None
        self._zone_id = None
        self._domain_name = None
        self._display_name = None
        self._rtypes = None
        self._compartment_id = None
        self.__self = None
        self._id = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def steering_policy_id(self):
        """
        **[Required]** Gets the steering_policy_id of this SteeringPolicyAttachment.
        The OCID of the attached steering policy.


        :return: The steering_policy_id of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._steering_policy_id

    @steering_policy_id.setter
    def steering_policy_id(self, steering_policy_id):
        """
        Sets the steering_policy_id of this SteeringPolicyAttachment.
        The OCID of the attached steering policy.


        :param steering_policy_id: The steering_policy_id of this SteeringPolicyAttachment.
        :type: str
        """
        self._steering_policy_id = steering_policy_id

    @property
    def zone_id(self):
        """
        **[Required]** Gets the zone_id of this SteeringPolicyAttachment.
        The OCID of the attached zone.


        :return: The zone_id of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this SteeringPolicyAttachment.
        The OCID of the attached zone.


        :param zone_id: The zone_id of this SteeringPolicyAttachment.
        :type: str
        """
        self._zone_id = zone_id

    @property
    def domain_name(self):
        """
        **[Required]** Gets the domain_name of this SteeringPolicyAttachment.
        The attached domain within the attached zone.


        :return: The domain_name of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this SteeringPolicyAttachment.
        The attached domain within the attached zone.


        :param domain_name: The domain_name of this SteeringPolicyAttachment.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SteeringPolicyAttachment.
        A user-friendly name for the steering policy attachment.
        Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :return: The display_name of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SteeringPolicyAttachment.
        A user-friendly name for the steering policy attachment.
        Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :param display_name: The display_name of this SteeringPolicyAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def rtypes(self):
        """
        **[Required]** Gets the rtypes of this SteeringPolicyAttachment.
        The record types covered by the attachment at the domain. The set of record types is
        determined by aggregating the record types from the answers defined in the steering
        policy.


        :return: The rtypes of this SteeringPolicyAttachment.
        :rtype: list[str]
        """
        return self._rtypes

    @rtypes.setter
    def rtypes(self, rtypes):
        """
        Sets the rtypes of this SteeringPolicyAttachment.
        The record types covered by the attachment at the domain. The set of record types is
        determined by aggregating the record types from the answers defined in the steering
        policy.


        :param rtypes: The rtypes of this SteeringPolicyAttachment.
        :type: list[str]
        """
        self._rtypes = rtypes

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SteeringPolicyAttachment.
        The OCID of the compartment containing the steering policy attachment.


        :return: The compartment_id of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SteeringPolicyAttachment.
        The OCID of the compartment containing the steering policy attachment.


        :param compartment_id: The compartment_id of this SteeringPolicyAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def _self(self):
        """
        **[Required]** Gets the _self of this SteeringPolicyAttachment.
        The canonical absolute URL of the resource.


        :return: The _self of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this SteeringPolicyAttachment.
        The canonical absolute URL of the resource.


        :param _self: The _self of this SteeringPolicyAttachment.
        :type: str
        """
        self.__self = _self

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SteeringPolicyAttachment.
        The OCID of the resource.


        :return: The id of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SteeringPolicyAttachment.
        The OCID of the resource.


        :param id: The id of this SteeringPolicyAttachment.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SteeringPolicyAttachment.
        The date and time the resource was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_created of this SteeringPolicyAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SteeringPolicyAttachment.
        The date and time the resource was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this SteeringPolicyAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SteeringPolicyAttachment.
        The current state of the resource.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SteeringPolicyAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SteeringPolicyAttachment.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this SteeringPolicyAttachment.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other