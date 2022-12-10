# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetAlertPolicyAssociationDetails(object):
    """
    The details used to update a target-alert policy association.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetAlertPolicyAssociationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateTargetAlertPolicyAssociationDetails.
        :type is_enabled: bool

        :param display_name:
            The value to assign to the display_name property of this UpdateTargetAlertPolicyAssociationDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateTargetAlertPolicyAssociationDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTargetAlertPolicyAssociationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTargetAlertPolicyAssociationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._is_enabled = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateTargetAlertPolicyAssociationDetails.
        Indicates if the target-alert policy association is enabled or disabled.


        :return: The is_enabled of this UpdateTargetAlertPolicyAssociationDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateTargetAlertPolicyAssociationDetails.
        Indicates if the target-alert policy association is enabled or disabled.


        :param is_enabled: The is_enabled of this UpdateTargetAlertPolicyAssociationDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateTargetAlertPolicyAssociationDetails.
        The display name of the target-alert policy association.


        :return: The display_name of this UpdateTargetAlertPolicyAssociationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateTargetAlertPolicyAssociationDetails.
        The display name of the target-alert policy association.


        :param display_name: The display_name of this UpdateTargetAlertPolicyAssociationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateTargetAlertPolicyAssociationDetails.
        Describes the target-alert policy association.


        :return: The description of this UpdateTargetAlertPolicyAssociationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateTargetAlertPolicyAssociationDetails.
        Describes the target-alert policy association.


        :param description: The description of this UpdateTargetAlertPolicyAssociationDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateTargetAlertPolicyAssociationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateTargetAlertPolicyAssociationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateTargetAlertPolicyAssociationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateTargetAlertPolicyAssociationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateTargetAlertPolicyAssociationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateTargetAlertPolicyAssociationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateTargetAlertPolicyAssociationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateTargetAlertPolicyAssociationDetails.
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
