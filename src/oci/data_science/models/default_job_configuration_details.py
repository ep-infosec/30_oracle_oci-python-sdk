# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .job_configuration_details import JobConfigurationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefaultJobConfigurationDetails(JobConfigurationDetails):
    """
    The default job configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DefaultJobConfigurationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.DefaultJobConfigurationDetails.job_type` attribute
        of this class is ``DEFAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_type:
            The value to assign to the job_type property of this DefaultJobConfigurationDetails.
            Allowed values for this property are: "DEFAULT"
        :type job_type: str

        :param environment_variables:
            The value to assign to the environment_variables property of this DefaultJobConfigurationDetails.
        :type environment_variables: dict(str, str)

        :param command_line_arguments:
            The value to assign to the command_line_arguments property of this DefaultJobConfigurationDetails.
        :type command_line_arguments: str

        :param maximum_runtime_in_minutes:
            The value to assign to the maximum_runtime_in_minutes property of this DefaultJobConfigurationDetails.
        :type maximum_runtime_in_minutes: int

        """
        self.swagger_types = {
            'job_type': 'str',
            'environment_variables': 'dict(str, str)',
            'command_line_arguments': 'str',
            'maximum_runtime_in_minutes': 'int'
        }

        self.attribute_map = {
            'job_type': 'jobType',
            'environment_variables': 'environmentVariables',
            'command_line_arguments': 'commandLineArguments',
            'maximum_runtime_in_minutes': 'maximumRuntimeInMinutes'
        }

        self._job_type = None
        self._environment_variables = None
        self._command_line_arguments = None
        self._maximum_runtime_in_minutes = None
        self._job_type = 'DEFAULT'

    @property
    def environment_variables(self):
        """
        Gets the environment_variables of this DefaultJobConfigurationDetails.
        Environment variables to set for the job.


        :return: The environment_variables of this DefaultJobConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables):
        """
        Sets the environment_variables of this DefaultJobConfigurationDetails.
        Environment variables to set for the job.


        :param environment_variables: The environment_variables of this DefaultJobConfigurationDetails.
        :type: dict(str, str)
        """
        self._environment_variables = environment_variables

    @property
    def command_line_arguments(self):
        """
        Gets the command_line_arguments of this DefaultJobConfigurationDetails.
        The arguments to pass to the job.


        :return: The command_line_arguments of this DefaultJobConfigurationDetails.
        :rtype: str
        """
        return self._command_line_arguments

    @command_line_arguments.setter
    def command_line_arguments(self, command_line_arguments):
        """
        Sets the command_line_arguments of this DefaultJobConfigurationDetails.
        The arguments to pass to the job.


        :param command_line_arguments: The command_line_arguments of this DefaultJobConfigurationDetails.
        :type: str
        """
        self._command_line_arguments = command_line_arguments

    @property
    def maximum_runtime_in_minutes(self):
        """
        Gets the maximum_runtime_in_minutes of this DefaultJobConfigurationDetails.
        A time bound for the execution of the job. Timer starts when the job becomes active.


        :return: The maximum_runtime_in_minutes of this DefaultJobConfigurationDetails.
        :rtype: int
        """
        return self._maximum_runtime_in_minutes

    @maximum_runtime_in_minutes.setter
    def maximum_runtime_in_minutes(self, maximum_runtime_in_minutes):
        """
        Sets the maximum_runtime_in_minutes of this DefaultJobConfigurationDetails.
        A time bound for the execution of the job. Timer starts when the job becomes active.


        :param maximum_runtime_in_minutes: The maximum_runtime_in_minutes of this DefaultJobConfigurationDetails.
        :type: int
        """
        self._maximum_runtime_in_minutes = maximum_runtime_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other