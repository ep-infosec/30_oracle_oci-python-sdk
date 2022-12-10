# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutoScalingConfigurationDetails(object):
    """
    UpdateAutoScalingConfigurationDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutoScalingConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAutoScalingConfigurationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateAutoScalingConfigurationDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAutoScalingConfigurationDetails.
        :type freeform_tags: dict(str, str)

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateAutoScalingConfigurationDetails.
        :type is_enabled: bool

        :param cool_down_in_seconds:
            The value to assign to the cool_down_in_seconds property of this UpdateAutoScalingConfigurationDetails.
        :type cool_down_in_seconds: int

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'is_enabled': 'bool',
            'cool_down_in_seconds': 'int'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'is_enabled': 'isEnabled',
            'cool_down_in_seconds': 'coolDownInSeconds'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._is_enabled = None
        self._cool_down_in_seconds = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAutoScalingConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAutoScalingConfigurationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAutoScalingConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAutoScalingConfigurationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutoScalingConfigurationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutoScalingConfigurationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAutoScalingConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAutoScalingConfigurationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAutoScalingConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAutoScalingConfigurationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAutoScalingConfigurationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateAutoScalingConfigurationDetails.
        Whether the autoscaling configuration is enabled.


        :return: The is_enabled of this UpdateAutoScalingConfigurationDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateAutoScalingConfigurationDetails.
        Whether the autoscaling configuration is enabled.


        :param is_enabled: The is_enabled of this UpdateAutoScalingConfigurationDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def cool_down_in_seconds(self):
        """
        Gets the cool_down_in_seconds of this UpdateAutoScalingConfigurationDetails.

        :return: The cool_down_in_seconds of this UpdateAutoScalingConfigurationDetails.
        :rtype: int
        """
        return self._cool_down_in_seconds

    @cool_down_in_seconds.setter
    def cool_down_in_seconds(self, cool_down_in_seconds):
        """
        Sets the cool_down_in_seconds of this UpdateAutoScalingConfigurationDetails.

        :param cool_down_in_seconds: The cool_down_in_seconds of this UpdateAutoScalingConfigurationDetails.
        :type: int
        """
        self._cool_down_in_seconds = cool_down_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other