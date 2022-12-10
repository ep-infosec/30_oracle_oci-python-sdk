# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWebAppAccelerationDetails(object):
    """
    The information about new WebAppAcceleration.
    """

    #: A constant which can be used with the backend_type property of a CreateWebAppAccelerationDetails.
    #: This constant has a value of "LOAD_BALANCER"
    BACKEND_TYPE_LOAD_BALANCER = "LOAD_BALANCER"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWebAppAccelerationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.waa.models.CreateWebAppAccelerationLoadBalancerDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateWebAppAccelerationDetails.
        :type display_name: str

        :param backend_type:
            The value to assign to the backend_type property of this CreateWebAppAccelerationDetails.
            Allowed values for this property are: "LOAD_BALANCER"
        :type backend_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateWebAppAccelerationDetails.
        :type compartment_id: str

        :param web_app_acceleration_policy_id:
            The value to assign to the web_app_acceleration_policy_id property of this CreateWebAppAccelerationDetails.
        :type web_app_acceleration_policy_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWebAppAccelerationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWebAppAccelerationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CreateWebAppAccelerationDetails.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'backend_type': 'str',
            'compartment_id': 'str',
            'web_app_acceleration_policy_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'backend_type': 'backendType',
            'compartment_id': 'compartmentId',
            'web_app_acceleration_policy_id': 'webAppAccelerationPolicyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._display_name = None
        self._backend_type = None
        self._compartment_id = None
        self._web_app_acceleration_policy_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['backendType']

        if type == 'LOAD_BALANCER':
            return 'CreateWebAppAccelerationLoadBalancerDetails'
        else:
            return 'CreateWebAppAccelerationDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateWebAppAccelerationDetails.
        WebAppAcceleration display name, can be renamed.


        :return: The display_name of this CreateWebAppAccelerationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateWebAppAccelerationDetails.
        WebAppAcceleration display name, can be renamed.


        :param display_name: The display_name of this CreateWebAppAccelerationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def backend_type(self):
        """
        **[Required]** Gets the backend_type of this CreateWebAppAccelerationDetails.
        Type of the WebAppFirewall, as example LOAD_BALANCER.

        Allowed values for this property are: "LOAD_BALANCER"


        :return: The backend_type of this CreateWebAppAccelerationDetails.
        :rtype: str
        """
        return self._backend_type

    @backend_type.setter
    def backend_type(self, backend_type):
        """
        Sets the backend_type of this CreateWebAppAccelerationDetails.
        Type of the WebAppFirewall, as example LOAD_BALANCER.


        :param backend_type: The backend_type of this CreateWebAppAccelerationDetails.
        :type: str
        """
        allowed_values = ["LOAD_BALANCER"]
        if not value_allowed_none_or_none_sentinel(backend_type, allowed_values):
            raise ValueError(
                "Invalid value for `backend_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._backend_type = backend_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateWebAppAccelerationDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateWebAppAccelerationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateWebAppAccelerationDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateWebAppAccelerationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def web_app_acceleration_policy_id(self):
        """
        **[Required]** Gets the web_app_acceleration_policy_id of this CreateWebAppAccelerationDetails.
        The `OCID`__ of WebAppAccelerationPolicy, which is attached to the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The web_app_acceleration_policy_id of this CreateWebAppAccelerationDetails.
        :rtype: str
        """
        return self._web_app_acceleration_policy_id

    @web_app_acceleration_policy_id.setter
    def web_app_acceleration_policy_id(self, web_app_acceleration_policy_id):
        """
        Sets the web_app_acceleration_policy_id of this CreateWebAppAccelerationDetails.
        The `OCID`__ of WebAppAccelerationPolicy, which is attached to the resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param web_app_acceleration_policy_id: The web_app_acceleration_policy_id of this CreateWebAppAccelerationDetails.
        :type: str
        """
        self._web_app_acceleration_policy_id = web_app_acceleration_policy_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateWebAppAccelerationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateWebAppAccelerationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateWebAppAccelerationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateWebAppAccelerationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateWebAppAccelerationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateWebAppAccelerationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateWebAppAccelerationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateWebAppAccelerationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CreateWebAppAccelerationDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this CreateWebAppAccelerationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CreateWebAppAccelerationDetails.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this CreateWebAppAccelerationDetails.
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
