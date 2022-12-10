# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociableEntity(object):
    """
    Entity details including whether or not it is eligible for association with the source.
    """

    #: A constant which can be used with the eligibility_status property of a AssociableEntity.
    #: This constant has a value of "ELIGIBLE"
    ELIGIBILITY_STATUS_ELIGIBLE = "ELIGIBLE"

    #: A constant which can be used with the eligibility_status property of a AssociableEntity.
    #: This constant has a value of "INELIGIBLE"
    ELIGIBILITY_STATUS_INELIGIBLE = "INELIGIBLE"

    def __init__(self, **kwargs):
        """
        Initializes a new AssociableEntity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_id:
            The value to assign to the entity_id property of this AssociableEntity.
        :type entity_id: str

        :param entity_name:
            The value to assign to the entity_name property of this AssociableEntity.
        :type entity_name: str

        :param entity_type_name:
            The value to assign to the entity_type_name property of this AssociableEntity.
        :type entity_type_name: str

        :param entity_type_display_name:
            The value to assign to the entity_type_display_name property of this AssociableEntity.
        :type entity_type_display_name: str

        :param host:
            The value to assign to the host property of this AssociableEntity.
        :type host: str

        :param agent_id:
            The value to assign to the agent_id property of this AssociableEntity.
        :type agent_id: str

        :param eligibility_status:
            The value to assign to the eligibility_status property of this AssociableEntity.
            Allowed values for this property are: "ELIGIBLE", "INELIGIBLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type eligibility_status: str

        :param ineligibility_details:
            The value to assign to the ineligibility_details property of this AssociableEntity.
        :type ineligibility_details: str

        """
        self.swagger_types = {
            'entity_id': 'str',
            'entity_name': 'str',
            'entity_type_name': 'str',
            'entity_type_display_name': 'str',
            'host': 'str',
            'agent_id': 'str',
            'eligibility_status': 'str',
            'ineligibility_details': 'str'
        }

        self.attribute_map = {
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'entity_type_name': 'entityTypeName',
            'entity_type_display_name': 'entityTypeDisplayName',
            'host': 'host',
            'agent_id': 'agentId',
            'eligibility_status': 'eligibilityStatus',
            'ineligibility_details': 'ineligibilityDetails'
        }

        self._entity_id = None
        self._entity_name = None
        self._entity_type_name = None
        self._entity_type_display_name = None
        self._host = None
        self._agent_id = None
        self._eligibility_status = None
        self._ineligibility_details = None

    @property
    def entity_id(self):
        """
        Gets the entity_id of this AssociableEntity.
        The entity OCID.


        :return: The entity_id of this AssociableEntity.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this AssociableEntity.
        The entity OCID.


        :param entity_id: The entity_id of this AssociableEntity.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def entity_name(self):
        """
        Gets the entity_name of this AssociableEntity.
        The name of the entity.


        :return: The entity_name of this AssociableEntity.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this AssociableEntity.
        The name of the entity.


        :param entity_name: The entity_name of this AssociableEntity.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def entity_type_name(self):
        """
        Gets the entity_type_name of this AssociableEntity.
        The type name of the entity.


        :return: The entity_type_name of this AssociableEntity.
        :rtype: str
        """
        return self._entity_type_name

    @entity_type_name.setter
    def entity_type_name(self, entity_type_name):
        """
        Sets the entity_type_name of this AssociableEntity.
        The type name of the entity.


        :param entity_type_name: The entity_type_name of this AssociableEntity.
        :type: str
        """
        self._entity_type_name = entity_type_name

    @property
    def entity_type_display_name(self):
        """
        Gets the entity_type_display_name of this AssociableEntity.
        The display name of the entity type.


        :return: The entity_type_display_name of this AssociableEntity.
        :rtype: str
        """
        return self._entity_type_display_name

    @entity_type_display_name.setter
    def entity_type_display_name(self, entity_type_display_name):
        """
        Sets the entity_type_display_name of this AssociableEntity.
        The display name of the entity type.


        :param entity_type_display_name: The entity_type_display_name of this AssociableEntity.
        :type: str
        """
        self._entity_type_display_name = entity_type_display_name

    @property
    def host(self):
        """
        Gets the host of this AssociableEntity.
        The entity host.


        :return: The host of this AssociableEntity.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this AssociableEntity.
        The entity host.


        :param host: The host of this AssociableEntity.
        :type: str
        """
        self._host = host

    @property
    def agent_id(self):
        """
        Gets the agent_id of this AssociableEntity.
        The OCID of the Management Agent.


        :return: The agent_id of this AssociableEntity.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this AssociableEntity.
        The OCID of the Management Agent.


        :param agent_id: The agent_id of this AssociableEntity.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def eligibility_status(self):
        """
        Gets the eligibility_status of this AssociableEntity.
        This field indicates whether the entity is (in)eligible to be associated with this source.

        Allowed values for this property are: "ELIGIBLE", "INELIGIBLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The eligibility_status of this AssociableEntity.
        :rtype: str
        """
        return self._eligibility_status

    @eligibility_status.setter
    def eligibility_status(self, eligibility_status):
        """
        Sets the eligibility_status of this AssociableEntity.
        This field indicates whether the entity is (in)eligible to be associated with this source.


        :param eligibility_status: The eligibility_status of this AssociableEntity.
        :type: str
        """
        allowed_values = ["ELIGIBLE", "INELIGIBLE"]
        if not value_allowed_none_or_none_sentinel(eligibility_status, allowed_values):
            eligibility_status = 'UNKNOWN_ENUM_VALUE'
        self._eligibility_status = eligibility_status

    @property
    def ineligibility_details(self):
        """
        Gets the ineligibility_details of this AssociableEntity.
        The reason the entity is not eligible for association.


        :return: The ineligibility_details of this AssociableEntity.
        :rtype: str
        """
        return self._ineligibility_details

    @ineligibility_details.setter
    def ineligibility_details(self, ineligibility_details):
        """
        Sets the ineligibility_details of this AssociableEntity.
        The reason the entity is not eligible for association.


        :param ineligibility_details: The ineligibility_details of this AssociableEntity.
        :type: str
        """
        self._ineligibility_details = ineligibility_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
