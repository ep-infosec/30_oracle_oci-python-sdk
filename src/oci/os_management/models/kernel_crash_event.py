# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .event import Event
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KernelCrashEvent(Event):
    """
    Information about a Kernel Crash.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KernelCrashEvent object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management.models.KernelCrashEvent.event_type` attribute
        of this class is ``KERNEL_CRASH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this KernelCrashEvent.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this KernelCrashEvent.
        :type instance_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this KernelCrashEvent.
        :type compartment_id: str

        :param tenancy_id:
            The value to assign to the tenancy_id property of this KernelCrashEvent.
        :type tenancy_id: str

        :param summary:
            The value to assign to the summary property of this KernelCrashEvent.
        :type summary: str

        :param timestamp:
            The value to assign to the timestamp property of this KernelCrashEvent.
        :type timestamp: datetime

        :param event_fingerprint:
            The value to assign to the event_fingerprint property of this KernelCrashEvent.
        :type event_fingerprint: str

        :param count:
            The value to assign to the count property of this KernelCrashEvent.
        :type count: int

        :param event_type:
            The value to assign to the event_type property of this KernelCrashEvent.
            Allowed values for this property are: "KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING"
        :type event_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this KernelCrashEvent.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this KernelCrashEvent.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this KernelCrashEvent.
        :type system_tags: dict(str, dict(str, object))

        :param reason:
            The value to assign to the reason property of this KernelCrashEvent.
        :type reason: str

        :param time_first_occurred:
            The value to assign to the time_first_occurred property of this KernelCrashEvent.
        :type time_first_occurred: datetime

        :param vmcore:
            The value to assign to the vmcore property of this KernelCrashEvent.
        :type vmcore: oci.os_management.models.KernelVmCoreInformation

        :param content:
            The value to assign to the content property of this KernelCrashEvent.
        :type content: oci.os_management.models.EventContent

        :param system:
            The value to assign to the system property of this KernelCrashEvent.
        :type system: oci.os_management.models.CrashEventSystemInformation

        """
        self.swagger_types = {
            'id': 'str',
            'instance_id': 'str',
            'compartment_id': 'str',
            'tenancy_id': 'str',
            'summary': 'str',
            'timestamp': 'datetime',
            'event_fingerprint': 'str',
            'count': 'int',
            'event_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'reason': 'str',
            'time_first_occurred': 'datetime',
            'vmcore': 'KernelVmCoreInformation',
            'content': 'EventContent',
            'system': 'CrashEventSystemInformation'
        }

        self.attribute_map = {
            'id': 'id',
            'instance_id': 'instanceId',
            'compartment_id': 'compartmentId',
            'tenancy_id': 'tenancyId',
            'summary': 'summary',
            'timestamp': 'timestamp',
            'event_fingerprint': 'eventFingerprint',
            'count': 'count',
            'event_type': 'eventType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'reason': 'reason',
            'time_first_occurred': 'timeFirstOccurred',
            'vmcore': 'vmcore',
            'content': 'content',
            'system': 'system'
        }

        self._id = None
        self._instance_id = None
        self._compartment_id = None
        self._tenancy_id = None
        self._summary = None
        self._timestamp = None
        self._event_fingerprint = None
        self._count = None
        self._event_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._reason = None
        self._time_first_occurred = None
        self._vmcore = None
        self._content = None
        self._system = None
        self._event_type = 'KERNEL_CRASH'

    @property
    def reason(self):
        """
        Gets the reason of this KernelCrashEvent.
        reason of the crash


        :return: The reason of this KernelCrashEvent.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this KernelCrashEvent.
        reason of the crash


        :param reason: The reason of this KernelCrashEvent.
        :type: str
        """
        self._reason = reason

    @property
    def time_first_occurred(self):
        """
        Gets the time_first_occurred of this KernelCrashEvent.
        First occurrence time of the event


        :return: The time_first_occurred of this KernelCrashEvent.
        :rtype: datetime
        """
        return self._time_first_occurred

    @time_first_occurred.setter
    def time_first_occurred(self, time_first_occurred):
        """
        Sets the time_first_occurred of this KernelCrashEvent.
        First occurrence time of the event


        :param time_first_occurred: The time_first_occurred of this KernelCrashEvent.
        :type: datetime
        """
        self._time_first_occurred = time_first_occurred

    @property
    def vmcore(self):
        """
        Gets the vmcore of this KernelCrashEvent.

        :return: The vmcore of this KernelCrashEvent.
        :rtype: oci.os_management.models.KernelVmCoreInformation
        """
        return self._vmcore

    @vmcore.setter
    def vmcore(self, vmcore):
        """
        Sets the vmcore of this KernelCrashEvent.

        :param vmcore: The vmcore of this KernelCrashEvent.
        :type: oci.os_management.models.KernelVmCoreInformation
        """
        self._vmcore = vmcore

    @property
    def content(self):
        """
        Gets the content of this KernelCrashEvent.

        :return: The content of this KernelCrashEvent.
        :rtype: oci.os_management.models.EventContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this KernelCrashEvent.

        :param content: The content of this KernelCrashEvent.
        :type: oci.os_management.models.EventContent
        """
        self._content = content

    @property
    def system(self):
        """
        Gets the system of this KernelCrashEvent.

        :return: The system of this KernelCrashEvent.
        :rtype: oci.os_management.models.CrashEventSystemInformation
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this KernelCrashEvent.

        :param system: The system of this KernelCrashEvent.
        :type: oci.os_management.models.CrashEventSystemInformation
        """
        self._system = system

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
