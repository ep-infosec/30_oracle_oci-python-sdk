# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompatibilityMessage(object):
    """
    Information about shape compatibility with the client's current resource configuration.
    """

    #: A constant which can be used with the severity property of a CompatibilityMessage.
    #: This constant has a value of "ERROR"
    SEVERITY_ERROR = "ERROR"

    #: A constant which can be used with the severity property of a CompatibilityMessage.
    #: This constant has a value of "WARNING"
    SEVERITY_WARNING = "WARNING"

    #: A constant which can be used with the severity property of a CompatibilityMessage.
    #: This constant has a value of "INFO"
    SEVERITY_INFO = "INFO"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "NOT_ENOUGH_DATA"
    NAME_NOT_ENOUGH_DATA = "NOT_ENOUGH_DATA"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "INVALID_DATA"
    NAME_INVALID_DATA = "INVALID_DATA"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "CPU_COMPATIBILITY_WARNING"
    NAME_CPU_COMPATIBILITY_WARNING = "CPU_COMPATIBILITY_WARNING"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "CPU_METRIC_INFO"
    NAME_CPU_METRIC_INFO = "CPU_METRIC_INFO"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "MEMORY_COMPATIBILITY_WARNING"
    NAME_MEMORY_COMPATIBILITY_WARNING = "MEMORY_COMPATIBILITY_WARNING"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "MEMORY_METRIC_INFO"
    NAME_MEMORY_METRIC_INFO = "MEMORY_METRIC_INFO"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "VNICS_COMPATIBILITY_WARNING"
    NAME_VNICS_COMPATIBILITY_WARNING = "VNICS_COMPATIBILITY_WARNING"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "BANDWIDTH_COMPATIBILITY_WARNING"
    NAME_BANDWIDTH_COMPATIBILITY_WARNING = "BANDWIDTH_COMPATIBILITY_WARNING"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "GPU_COMPATIBILITY_WARNING"
    NAME_GPU_COMPATIBILITY_WARNING = "GPU_COMPATIBILITY_WARNING"

    #: A constant which can be used with the name property of a CompatibilityMessage.
    #: This constant has a value of "OS_WARNING"
    NAME_OS_WARNING = "OS_WARNING"

    def __init__(self, **kwargs):
        """
        Initializes a new CompatibilityMessage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param severity:
            The value to assign to the severity property of this CompatibilityMessage.
            Allowed values for this property are: "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type severity: str

        :param name:
            The value to assign to the name property of this CompatibilityMessage.
            Allowed values for this property are: "NOT_ENOUGH_DATA", "INVALID_DATA", "CPU_COMPATIBILITY_WARNING", "CPU_METRIC_INFO", "MEMORY_COMPATIBILITY_WARNING", "MEMORY_METRIC_INFO", "VNICS_COMPATIBILITY_WARNING", "BANDWIDTH_COMPATIBILITY_WARNING", "GPU_COMPATIBILITY_WARNING", "OS_WARNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param message:
            The value to assign to the message property of this CompatibilityMessage.
        :type message: str

        """
        self.swagger_types = {
            'severity': 'str',
            'name': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'severity': 'severity',
            'name': 'name',
            'message': 'message'
        }

        self._severity = None
        self._name = None
        self._message = None

    @property
    def severity(self):
        """
        Gets the severity of this CompatibilityMessage.
        Severity level of the compatibility issue.

        Allowed values for this property are: "ERROR", "WARNING", "INFO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The severity of this CompatibilityMessage.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this CompatibilityMessage.
        Severity level of the compatibility issue.


        :param severity: The severity of this CompatibilityMessage.
        :type: str
        """
        allowed_values = ["ERROR", "WARNING", "INFO"]
        if not value_allowed_none_or_none_sentinel(severity, allowed_values):
            severity = 'UNKNOWN_ENUM_VALUE'
        self._severity = severity

    @property
    def name(self):
        """
        Gets the name of this CompatibilityMessage.
        Name of the compatibility issue.

        Allowed values for this property are: "NOT_ENOUGH_DATA", "INVALID_DATA", "CPU_COMPATIBILITY_WARNING", "CPU_METRIC_INFO", "MEMORY_COMPATIBILITY_WARNING", "MEMORY_METRIC_INFO", "VNICS_COMPATIBILITY_WARNING", "BANDWIDTH_COMPATIBILITY_WARNING", "GPU_COMPATIBILITY_WARNING", "OS_WARNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this CompatibilityMessage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CompatibilityMessage.
        Name of the compatibility issue.


        :param name: The name of this CompatibilityMessage.
        :type: str
        """
        allowed_values = ["NOT_ENOUGH_DATA", "INVALID_DATA", "CPU_COMPATIBILITY_WARNING", "CPU_METRIC_INFO", "MEMORY_COMPATIBILITY_WARNING", "MEMORY_METRIC_INFO", "VNICS_COMPATIBILITY_WARNING", "BANDWIDTH_COMPATIBILITY_WARNING", "GPU_COMPATIBILITY_WARNING", "OS_WARNING"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def message(self):
        """
        Gets the message of this CompatibilityMessage.
        Detailed description of the compatibility issue.


        :return: The message of this CompatibilityMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CompatibilityMessage.
        Detailed description of the compatibility issue.


        :param message: The message of this CompatibilityMessage.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
