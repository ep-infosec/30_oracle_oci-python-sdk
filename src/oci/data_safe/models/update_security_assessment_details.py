# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSecurityAssessmentDetails(object):
    """
    Updates one or more attributes of the specified security assessment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSecurityAssessmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateSecurityAssessmentDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateSecurityAssessmentDetails.
        :type description: str

        :param schedule:
            The value to assign to the schedule property of this UpdateSecurityAssessmentDetails.
        :type schedule: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateSecurityAssessmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateSecurityAssessmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'schedule': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'schedule': 'schedule',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._schedule = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateSecurityAssessmentDetails.
        The display name of the security assessment.


        :return: The display_name of this UpdateSecurityAssessmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateSecurityAssessmentDetails.
        The display name of the security assessment.


        :param display_name: The display_name of this UpdateSecurityAssessmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateSecurityAssessmentDetails.
        The description of the security assessment.


        :return: The description of this UpdateSecurityAssessmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateSecurityAssessmentDetails.
        The description of the security assessment.


        :param description: The description of this UpdateSecurityAssessmentDetails.
        :type: str
        """
        self._description = description

    @property
    def schedule(self):
        """
        Gets the schedule of this UpdateSecurityAssessmentDetails.
        This is applicable only for save schedule and latest assessment. It updates the existing schedule in a specified format:
        <version-string>;<version-specific-schedule>

        Allowed version strings - \"v1\"
        v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
        Each of the above fields potentially introduce constraints. A workrequest is created only
        when clock time satisfies all the constraints. Constraints introduced:
        1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
        2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
        3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
        <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
        4. No constraint introduced when it is '*'. When not, day of week must equal the given value
        <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
        5. No constraint introduced when it is '*'. When not, day of month must equal the given value


        :return: The schedule of this UpdateSecurityAssessmentDetails.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this UpdateSecurityAssessmentDetails.
        This is applicable only for save schedule and latest assessment. It updates the existing schedule in a specified format:
        <version-string>;<version-specific-schedule>

        Allowed version strings - \"v1\"
        v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
        Each of the above fields potentially introduce constraints. A workrequest is created only
        when clock time satisfies all the constraints. Constraints introduced:
        1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
        2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
        3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
        <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
        4. No constraint introduced when it is '*'. When not, day of week must equal the given value
        <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
        5. No constraint introduced when it is '*'. When not, day of month must equal the given value


        :param schedule: The schedule of this UpdateSecurityAssessmentDetails.
        :type: str
        """
        self._schedule = schedule

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateSecurityAssessmentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateSecurityAssessmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateSecurityAssessmentDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateSecurityAssessmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateSecurityAssessmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateSecurityAssessmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateSecurityAssessmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateSecurityAssessmentDetails.
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
