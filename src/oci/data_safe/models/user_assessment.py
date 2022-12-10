# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserAssessment(object):
    """
    The details of the user assessment, which includes statistics related to target database users.
    """

    #: A constant which can be used with the lifecycle_state property of a UserAssessment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a UserAssessment.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a UserAssessment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a UserAssessment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a UserAssessment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a UserAssessment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the triggered_by property of a UserAssessment.
    #: This constant has a value of "USER"
    TRIGGERED_BY_USER = "USER"

    #: A constant which can be used with the triggered_by property of a UserAssessment.
    #: This constant has a value of "SYSTEM"
    TRIGGERED_BY_SYSTEM = "SYSTEM"

    #: A constant which can be used with the type property of a UserAssessment.
    #: This constant has a value of "LATEST"
    TYPE_LATEST = "LATEST"

    #: A constant which can be used with the type property of a UserAssessment.
    #: This constant has a value of "SAVED"
    TYPE_SAVED = "SAVED"

    #: A constant which can be used with the type property of a UserAssessment.
    #: This constant has a value of "SAVE_SCHEDULE"
    TYPE_SAVE_SCHEDULE = "SAVE_SCHEDULE"

    #: A constant which can be used with the type property of a UserAssessment.
    #: This constant has a value of "COMPARTMENT"
    TYPE_COMPARTMENT = "COMPARTMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new UserAssessment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UserAssessment.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this UserAssessment.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UserAssessment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this UserAssessment.
        :type id: str

        :param ignored_targets:
            The value to assign to the ignored_targets property of this UserAssessment.
        :type ignored_targets: list[object]

        :param ignored_assessment_ids:
            The value to assign to the ignored_assessment_ids property of this UserAssessment.
        :type ignored_assessment_ids: list[object]

        :param is_baseline:
            The value to assign to the is_baseline property of this UserAssessment.
        :type is_baseline: bool

        :param is_deviated_from_baseline:
            The value to assign to the is_deviated_from_baseline property of this UserAssessment.
        :type is_deviated_from_baseline: bool

        :param last_compared_baseline_id:
            The value to assign to the last_compared_baseline_id property of this UserAssessment.
        :type last_compared_baseline_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UserAssessment.
            Allowed values for this property are: "CREATING", "SUCCEEDED", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this UserAssessment.
        :type lifecycle_details: str

        :param schedule_assessment_id:
            The value to assign to the schedule_assessment_id property of this UserAssessment.
        :type schedule_assessment_id: str

        :param schedule:
            The value to assign to the schedule property of this UserAssessment.
        :type schedule: str

        :param statistics:
            The value to assign to the statistics property of this UserAssessment.
        :type statistics: dict(str, dict(str, object))

        :param target_ids:
            The value to assign to the target_ids property of this UserAssessment.
        :type target_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this UserAssessment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this UserAssessment.
        :type time_updated: datetime

        :param triggered_by:
            The value to assign to the triggered_by property of this UserAssessment.
            Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type triggered_by: str

        :param type:
            The value to assign to the type property of this UserAssessment.
            Allowed values for this property are: "LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UserAssessment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UserAssessment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this UserAssessment.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'description': 'str',
            'display_name': 'str',
            'id': 'str',
            'ignored_targets': 'list[object]',
            'ignored_assessment_ids': 'list[object]',
            'is_baseline': 'bool',
            'is_deviated_from_baseline': 'bool',
            'last_compared_baseline_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'schedule_assessment_id': 'str',
            'schedule': 'str',
            'statistics': 'dict(str, dict(str, object))',
            'target_ids': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'triggered_by': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'description': 'description',
            'display_name': 'displayName',
            'id': 'id',
            'ignored_targets': 'ignoredTargets',
            'ignored_assessment_ids': 'ignoredAssessmentIds',
            'is_baseline': 'isBaseline',
            'is_deviated_from_baseline': 'isDeviatedFromBaseline',
            'last_compared_baseline_id': 'lastComparedBaselineId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'schedule_assessment_id': 'scheduleAssessmentId',
            'schedule': 'schedule',
            'statistics': 'statistics',
            'target_ids': 'targetIds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'triggered_by': 'triggeredBy',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._compartment_id = None
        self._description = None
        self._display_name = None
        self._id = None
        self._ignored_targets = None
        self._ignored_assessment_ids = None
        self._is_baseline = None
        self._is_deviated_from_baseline = None
        self._last_compared_baseline_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._schedule_assessment_id = None
        self._schedule = None
        self._statistics = None
        self._target_ids = None
        self._time_created = None
        self._time_updated = None
        self._triggered_by = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this UserAssessment.
        The OCID of the compartment that contains the user assessment.


        :return: The compartment_id of this UserAssessment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UserAssessment.
        The OCID of the compartment that contains the user assessment.


        :param compartment_id: The compartment_id of this UserAssessment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this UserAssessment.
        The description of the user assessment.


        :return: The description of this UserAssessment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserAssessment.
        The description of the user assessment.


        :param description: The description of this UserAssessment.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this UserAssessment.
        The display name of the user assessment.


        :return: The display_name of this UserAssessment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UserAssessment.
        The display name of the user assessment.


        :param display_name: The display_name of this UserAssessment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this UserAssessment.
        The OCID of the user assessment.


        :return: The id of this UserAssessment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserAssessment.
        The OCID of the user assessment.


        :param id: The id of this UserAssessment.
        :type: str
        """
        self._id = id

    @property
    def ignored_targets(self):
        """
        Gets the ignored_targets of this UserAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :return: The ignored_targets of this UserAssessment.
        :rtype: list[object]
        """
        return self._ignored_targets

    @ignored_targets.setter
    def ignored_targets(self, ignored_targets):
        """
        Sets the ignored_targets of this UserAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :param ignored_targets: The ignored_targets of this UserAssessment.
        :type: list[object]
        """
        self._ignored_targets = ignored_targets

    @property
    def ignored_assessment_ids(self):
        """
        Gets the ignored_assessment_ids of this UserAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :return: The ignored_assessment_ids of this UserAssessment.
        :rtype: list[object]
        """
        return self._ignored_assessment_ids

    @ignored_assessment_ids.setter
    def ignored_assessment_ids(self, ignored_assessment_ids):
        """
        Sets the ignored_assessment_ids of this UserAssessment.
        List containing maps as values.
        Example: `{\"Operations\": [ {\"CostCenter\": \"42\"} ] }`


        :param ignored_assessment_ids: The ignored_assessment_ids of this UserAssessment.
        :type: list[object]
        """
        self._ignored_assessment_ids = ignored_assessment_ids

    @property
    def is_baseline(self):
        """
        Gets the is_baseline of this UserAssessment.
        Indicates if the user assessment is set as a baseline. This is applicable only to saved user assessments.


        :return: The is_baseline of this UserAssessment.
        :rtype: bool
        """
        return self._is_baseline

    @is_baseline.setter
    def is_baseline(self, is_baseline):
        """
        Sets the is_baseline of this UserAssessment.
        Indicates if the user assessment is set as a baseline. This is applicable only to saved user assessments.


        :param is_baseline: The is_baseline of this UserAssessment.
        :type: bool
        """
        self._is_baseline = is_baseline

    @property
    def is_deviated_from_baseline(self):
        """
        Gets the is_deviated_from_baseline of this UserAssessment.
        Indicates if the user assessment deviates from the baseline.


        :return: The is_deviated_from_baseline of this UserAssessment.
        :rtype: bool
        """
        return self._is_deviated_from_baseline

    @is_deviated_from_baseline.setter
    def is_deviated_from_baseline(self, is_deviated_from_baseline):
        """
        Sets the is_deviated_from_baseline of this UserAssessment.
        Indicates if the user assessment deviates from the baseline.


        :param is_deviated_from_baseline: The is_deviated_from_baseline of this UserAssessment.
        :type: bool
        """
        self._is_deviated_from_baseline = is_deviated_from_baseline

    @property
    def last_compared_baseline_id(self):
        """
        Gets the last_compared_baseline_id of this UserAssessment.
        The OCID of the last user assessment baseline against which the latest assessment was compared.


        :return: The last_compared_baseline_id of this UserAssessment.
        :rtype: str
        """
        return self._last_compared_baseline_id

    @last_compared_baseline_id.setter
    def last_compared_baseline_id(self, last_compared_baseline_id):
        """
        Sets the last_compared_baseline_id of this UserAssessment.
        The OCID of the last user assessment baseline against which the latest assessment was compared.


        :param last_compared_baseline_id: The last_compared_baseline_id of this UserAssessment.
        :type: str
        """
        self._last_compared_baseline_id = last_compared_baseline_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this UserAssessment.
        The current state of the user assessment.

        Allowed values for this property are: "CREATING", "SUCCEEDED", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this UserAssessment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UserAssessment.
        The current state of the user assessment.


        :param lifecycle_state: The lifecycle_state of this UserAssessment.
        :type: str
        """
        allowed_values = ["CREATING", "SUCCEEDED", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this UserAssessment.
        Details about the current state of the user assessment.


        :return: The lifecycle_details of this UserAssessment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this UserAssessment.
        Details about the current state of the user assessment.


        :param lifecycle_details: The lifecycle_details of this UserAssessment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def schedule_assessment_id(self):
        """
        Gets the schedule_assessment_id of this UserAssessment.
        The OCID of the user assessment that is responsible for creating this scheduled save assessment.


        :return: The schedule_assessment_id of this UserAssessment.
        :rtype: str
        """
        return self._schedule_assessment_id

    @schedule_assessment_id.setter
    def schedule_assessment_id(self, schedule_assessment_id):
        """
        Sets the schedule_assessment_id of this UserAssessment.
        The OCID of the user assessment that is responsible for creating this scheduled save assessment.


        :param schedule_assessment_id: The schedule_assessment_id of this UserAssessment.
        :type: str
        """
        self._schedule_assessment_id = schedule_assessment_id

    @property
    def schedule(self):
        """
        Gets the schedule of this UserAssessment.
        Schedule of the assessment that runs periodically in this specified format:
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


        :return: The schedule of this UserAssessment.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this UserAssessment.
        Schedule of the assessment that runs periodically in this specified format:
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


        :param schedule: The schedule of this UserAssessment.
        :type: str
        """
        self._schedule = schedule

    @property
    def statistics(self):
        """
        Gets the statistics of this UserAssessment.
        Map that contains maps of values.
         Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The statistics of this UserAssessment.
        :rtype: dict(str, dict(str, object))
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this UserAssessment.
        Map that contains maps of values.
         Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param statistics: The statistics of this UserAssessment.
        :type: dict(str, dict(str, object))
        """
        self._statistics = statistics

    @property
    def target_ids(self):
        """
        Gets the target_ids of this UserAssessment.
        Array of database target OCIDs.


        :return: The target_ids of this UserAssessment.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        """
        Sets the target_ids of this UserAssessment.
        Array of database target OCIDs.


        :param target_ids: The target_ids of this UserAssessment.
        :type: list[str]
        """
        self._target_ids = target_ids

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this UserAssessment.
        The date and time the user assessment was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this UserAssessment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UserAssessment.
        The date and time the user assessment was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this UserAssessment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this UserAssessment.
        The date and time the user assessment was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this UserAssessment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this UserAssessment.
        The date and time the user assessment was last updated, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this UserAssessment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def triggered_by(self):
        """
        Gets the triggered_by of this UserAssessment.
        Indicates whether the user assessment was created by system or user.

        Allowed values for this property are: "USER", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The triggered_by of this UserAssessment.
        :rtype: str
        """
        return self._triggered_by

    @triggered_by.setter
    def triggered_by(self, triggered_by):
        """
        Sets the triggered_by of this UserAssessment.
        Indicates whether the user assessment was created by system or user.


        :param triggered_by: The triggered_by of this UserAssessment.
        :type: str
        """
        allowed_values = ["USER", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(triggered_by, allowed_values):
            triggered_by = 'UNKNOWN_ENUM_VALUE'
        self._triggered_by = triggered_by

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UserAssessment.
        Type of user assessment. Type can be:

        LATEST: The most up-to-date assessment that is running automatically for a target. It is system generated.
        SAVED: A saved user assessment. LATEST assessments will always be saved to maintain the history of runs. A SAVED assessment is also generated by a 'refresh' action (triggered by the user).
        SAVE_SCHEDULE: A schedule to periodically save LATEST assessments.
        COMPARTMENT: An automatic managed assessment type that stores all details of targets in one compartment. This will keep an up-to-date status of all potential risks identified in the compartment.
               It is automatically updated once the latest assessment or refresh action is executed, as well as when a target is deleted or moved to a different compartment.

        Allowed values for this property are: "LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this UserAssessment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserAssessment.
        Type of user assessment. Type can be:

        LATEST: The most up-to-date assessment that is running automatically for a target. It is system generated.
        SAVED: A saved user assessment. LATEST assessments will always be saved to maintain the history of runs. A SAVED assessment is also generated by a 'refresh' action (triggered by the user).
        SAVE_SCHEDULE: A schedule to periodically save LATEST assessments.
        COMPARTMENT: An automatic managed assessment type that stores all details of targets in one compartment. This will keep an up-to-date status of all potential risks identified in the compartment.
               It is automatically updated once the latest assessment or refresh action is executed, as well as when a target is deleted or moved to a different compartment.


        :param type: The type of this UserAssessment.
        :type: str
        """
        allowed_values = ["LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UserAssessment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UserAssessment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UserAssessment.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UserAssessment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UserAssessment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UserAssessment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UserAssessment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UserAssessment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this UserAssessment.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this UserAssessment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this UserAssessment.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this UserAssessment.
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
