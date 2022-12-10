# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplicationSummary(object):
    """
    Summary of the Vb Instance's applications.
    """

    #: A constant which can be used with the state property of a ApplicationSummary.
    #: This constant has a value of "STAGE"
    STATE_STAGE = "STAGE"

    #: A constant which can be used with the state property of a ApplicationSummary.
    #: This constant has a value of "LIVE"
    STATE_LIVE = "LIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ApplicationSummary.
        :type id: str

        :param project_id:
            The value to assign to the project_id property of this ApplicationSummary.
        :type project_id: str

        :param version:
            The value to assign to the version property of this ApplicationSummary.
        :type version: str

        :param state:
            The value to assign to the state property of this ApplicationSummary.
            Allowed values for this property are: "STAGE", "LIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        """
        self.swagger_types = {
            'id': 'str',
            'project_id': 'str',
            'version': 'str',
            'state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'project_id': 'projectId',
            'version': 'version',
            'state': 'state'
        }

        self._id = None
        self._project_id = None
        self._version = None
        self._state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ApplicationSummary.
        Unique identifier of the application.


        :return: The id of this ApplicationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApplicationSummary.
        Unique identifier of the application.


        :param id: The id of this ApplicationSummary.
        :type: str
        """
        self._id = id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this ApplicationSummary.
        Project identifier.


        :return: The project_id of this ApplicationSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this ApplicationSummary.
        Project identifier.


        :param project_id: The project_id of this ApplicationSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def version(self):
        """
        **[Required]** Gets the version of this ApplicationSummary.
        Version of deployed application.


        :return: The version of this ApplicationSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ApplicationSummary.
        Version of deployed application.


        :param version: The version of this ApplicationSummary.
        :type: str
        """
        self._version = version

    @property
    def state(self):
        """
        **[Required]** Gets the state of this ApplicationSummary.
        Represents the deployment state of the application.

        Allowed values for this property are: "STAGE", "LIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this ApplicationSummary.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ApplicationSummary.
        Represents the deployment state of the application.


        :param state: The state of this ApplicationSummary.
        :type: str
        """
        allowed_values = ["STAGE", "LIVE"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
