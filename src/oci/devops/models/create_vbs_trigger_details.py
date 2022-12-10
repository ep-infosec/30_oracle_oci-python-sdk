# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_trigger_details import CreateTriggerDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVbsTriggerDetails(CreateTriggerDetails):
    """
    The trigger for VBS as the caller.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVbsTriggerDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateVbsTriggerDetails.trigger_source` attribute
        of this class is ``VBS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateVbsTriggerDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateVbsTriggerDetails.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this CreateVbsTriggerDetails.
        :type project_id: str

        :param trigger_source:
            The value to assign to the trigger_source property of this CreateVbsTriggerDetails.
        :type trigger_source: str

        :param actions:
            The value to assign to the actions property of this CreateVbsTriggerDetails.
        :type actions: list[oci.devops.models.TriggerAction]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateVbsTriggerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateVbsTriggerDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param connection_id:
            The value to assign to the connection_id property of this CreateVbsTriggerDetails.
        :type connection_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'trigger_source': 'str',
            'actions': 'list[TriggerAction]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'connection_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'trigger_source': 'triggerSource',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'connection_id': 'connectionId'
        }

        self._display_name = None
        self._description = None
        self._project_id = None
        self._trigger_source = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._connection_id = None
        self._trigger_source = 'VBS'

    @property
    def connection_id(self):
        """
        Gets the connection_id of this CreateVbsTriggerDetails.
        The OCID of the connection resource used to get details for triggered events.


        :return: The connection_id of this CreateVbsTriggerDetails.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this CreateVbsTriggerDetails.
        The OCID of the connection resource used to get details for triggered events.


        :param connection_id: The connection_id of this CreateVbsTriggerDetails.
        :type: str
        """
        self._connection_id = connection_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
