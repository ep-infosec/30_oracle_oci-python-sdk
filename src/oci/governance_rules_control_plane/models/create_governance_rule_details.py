# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGovernanceRuleDetails(object):
    """
    Request object for CreateGovernanceRule operation.
    """

    #: A constant which can be used with the type property of a CreateGovernanceRuleDetails.
    #: This constant has a value of "QUOTA"
    TYPE_QUOTA = "QUOTA"

    #: A constant which can be used with the type property of a CreateGovernanceRuleDetails.
    #: This constant has a value of "TAG"
    TYPE_TAG = "TAG"

    #: A constant which can be used with the type property of a CreateGovernanceRuleDetails.
    #: This constant has a value of "ALLOWED_REGIONS"
    TYPE_ALLOWED_REGIONS = "ALLOWED_REGIONS"

    #: A constant which can be used with the creation_option property of a CreateGovernanceRuleDetails.
    #: This constant has a value of "TEMPLATE"
    CREATION_OPTION_TEMPLATE = "TEMPLATE"

    #: A constant which can be used with the creation_option property of a CreateGovernanceRuleDetails.
    #: This constant has a value of "CLONE"
    CREATION_OPTION_CLONE = "CLONE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGovernanceRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateGovernanceRuleDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateGovernanceRuleDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateGovernanceRuleDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this CreateGovernanceRuleDetails.
            Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS"
        :type type: str

        :param creation_option:
            The value to assign to the creation_option property of this CreateGovernanceRuleDetails.
            Allowed values for this property are: "TEMPLATE", "CLONE"
        :type creation_option: str

        :param template:
            The value to assign to the template property of this CreateGovernanceRuleDetails.
        :type template: oci.governance_rules_control_plane.models.Template

        :param related_resource_id:
            The value to assign to the related_resource_id property of this CreateGovernanceRuleDetails.
        :type related_resource_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateGovernanceRuleDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateGovernanceRuleDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'creation_option': 'str',
            'template': 'Template',
            'related_resource_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'creation_option': 'creationOption',
            'template': 'template',
            'related_resource_id': 'relatedResourceId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._type = None
        self._creation_option = None
        self._template = None
        self._related_resource_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateGovernanceRuleDetails.
        The Oracle ID (`OCID`__) of the root compartment containing the governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateGovernanceRuleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateGovernanceRuleDetails.
        The Oracle ID (`OCID`__) of the root compartment containing the governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateGovernanceRuleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateGovernanceRuleDetails.
        Display name of the governance rule.


        :return: The display_name of this CreateGovernanceRuleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateGovernanceRuleDetails.
        Display name of the governance rule.


        :param display_name: The display_name of this CreateGovernanceRuleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateGovernanceRuleDetails.
        Description of the governance rule.


        :return: The description of this CreateGovernanceRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateGovernanceRuleDetails.
        Description of the governance rule.


        :param description: The description of this CreateGovernanceRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateGovernanceRuleDetails.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`

        Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS"


        :return: The type of this CreateGovernanceRuleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateGovernanceRuleDetails.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`


        :param type: The type of this CreateGovernanceRuleDetails.
        :type: str
        """
        allowed_values = ["QUOTA", "TAG", "ALLOWED_REGIONS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def creation_option(self):
        """
        **[Required]** Gets the creation_option of this CreateGovernanceRuleDetails.
        The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

        Example: `TEMPLATE`

        Allowed values for this property are: "TEMPLATE", "CLONE"


        :return: The creation_option of this CreateGovernanceRuleDetails.
        :rtype: str
        """
        return self._creation_option

    @creation_option.setter
    def creation_option(self, creation_option):
        """
        Sets the creation_option of this CreateGovernanceRuleDetails.
        The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

        Example: `TEMPLATE`


        :param creation_option: The creation_option of this CreateGovernanceRuleDetails.
        :type: str
        """
        allowed_values = ["TEMPLATE", "CLONE"]
        if not value_allowed_none_or_none_sentinel(creation_option, allowed_values):
            raise ValueError(
                "Invalid value for `creation_option`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._creation_option = creation_option

    @property
    def template(self):
        """
        **[Required]** Gets the template of this CreateGovernanceRuleDetails.

        :return: The template of this CreateGovernanceRuleDetails.
        :rtype: oci.governance_rules_control_plane.models.Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CreateGovernanceRuleDetails.

        :param template: The template of this CreateGovernanceRuleDetails.
        :type: oci.governance_rules_control_plane.models.Template
        """
        self._template = template

    @property
    def related_resource_id(self):
        """
        Gets the related_resource_id of this CreateGovernanceRuleDetails.
        The Oracle ID (`OCID`__) of the resource, which was used as a template to create this governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The related_resource_id of this CreateGovernanceRuleDetails.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this CreateGovernanceRuleDetails.
        The Oracle ID (`OCID`__) of the resource, which was used as a template to create this governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param related_resource_id: The related_resource_id of this CreateGovernanceRuleDetails.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateGovernanceRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateGovernanceRuleDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateGovernanceRuleDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateGovernanceRuleDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateGovernanceRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateGovernanceRuleDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateGovernanceRuleDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateGovernanceRuleDetails.
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
