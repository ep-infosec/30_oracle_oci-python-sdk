# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParserFunctionParameter(object):
    """
    LogAnalyticsParserFunctionParameter
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParserFunctionParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_function_id:
            The value to assign to the parser_function_id property of this LogAnalyticsParserFunctionParameter.
        :type parser_function_id: int

        :param parser_function_parameter_name:
            The value to assign to the parser_function_parameter_name property of this LogAnalyticsParserFunctionParameter.
        :type parser_function_parameter_name: str

        :param parser_function_parameter_id:
            The value to assign to the parser_function_parameter_id property of this LogAnalyticsParserFunctionParameter.
        :type parser_function_parameter_id: int

        :param parser_meta_plugin_parameter_name:
            The value to assign to the parser_meta_plugin_parameter_name property of this LogAnalyticsParserFunctionParameter.
        :type parser_meta_plugin_parameter_name: str

        :param parser_meta_plugin_parameter_value:
            The value to assign to the parser_meta_plugin_parameter_value property of this LogAnalyticsParserFunctionParameter.
        :type parser_meta_plugin_parameter_value: str

        :param parser_name:
            The value to assign to the parser_name property of this LogAnalyticsParserFunctionParameter.
        :type parser_name: str

        :param parser_meta_plugin_parameter:
            The value to assign to the parser_meta_plugin_parameter property of this LogAnalyticsParserFunctionParameter.
        :type parser_meta_plugin_parameter: oci.log_analytics.models.LogAnalyticsParserMetaPluginParameter

        """
        self.swagger_types = {
            'parser_function_id': 'int',
            'parser_function_parameter_name': 'str',
            'parser_function_parameter_id': 'int',
            'parser_meta_plugin_parameter_name': 'str',
            'parser_meta_plugin_parameter_value': 'str',
            'parser_name': 'str',
            'parser_meta_plugin_parameter': 'LogAnalyticsParserMetaPluginParameter'
        }

        self.attribute_map = {
            'parser_function_id': 'parserFunctionId',
            'parser_function_parameter_name': 'parserFunctionParameterName',
            'parser_function_parameter_id': 'parserFunctionParameterId',
            'parser_meta_plugin_parameter_name': 'parserMetaPluginParameterName',
            'parser_meta_plugin_parameter_value': 'parserMetaPluginParameterValue',
            'parser_name': 'parserName',
            'parser_meta_plugin_parameter': 'parserMetaPluginParameter'
        }

        self._parser_function_id = None
        self._parser_function_parameter_name = None
        self._parser_function_parameter_id = None
        self._parser_meta_plugin_parameter_name = None
        self._parser_meta_plugin_parameter_value = None
        self._parser_name = None
        self._parser_meta_plugin_parameter = None

    @property
    def parser_function_id(self):
        """
        Gets the parser_function_id of this LogAnalyticsParserFunctionParameter.
        The parser function unique identifier.


        :return: The parser_function_id of this LogAnalyticsParserFunctionParameter.
        :rtype: int
        """
        return self._parser_function_id

    @parser_function_id.setter
    def parser_function_id(self, parser_function_id):
        """
        Sets the parser_function_id of this LogAnalyticsParserFunctionParameter.
        The parser function unique identifier.


        :param parser_function_id: The parser_function_id of this LogAnalyticsParserFunctionParameter.
        :type: int
        """
        self._parser_function_id = parser_function_id

    @property
    def parser_function_parameter_name(self):
        """
        Gets the parser_function_parameter_name of this LogAnalyticsParserFunctionParameter.
        The internal name


        :return: The parser_function_parameter_name of this LogAnalyticsParserFunctionParameter.
        :rtype: str
        """
        return self._parser_function_parameter_name

    @parser_function_parameter_name.setter
    def parser_function_parameter_name(self, parser_function_parameter_name):
        """
        Sets the parser_function_parameter_name of this LogAnalyticsParserFunctionParameter.
        The internal name


        :param parser_function_parameter_name: The parser_function_parameter_name of this LogAnalyticsParserFunctionParameter.
        :type: str
        """
        self._parser_function_parameter_name = parser_function_parameter_name

    @property
    def parser_function_parameter_id(self):
        """
        Gets the parser_function_parameter_id of this LogAnalyticsParserFunctionParameter.
        The parameter unique identifier.


        :return: The parser_function_parameter_id of this LogAnalyticsParserFunctionParameter.
        :rtype: int
        """
        return self._parser_function_parameter_id

    @parser_function_parameter_id.setter
    def parser_function_parameter_id(self, parser_function_parameter_id):
        """
        Sets the parser_function_parameter_id of this LogAnalyticsParserFunctionParameter.
        The parameter unique identifier.


        :param parser_function_parameter_id: The parser_function_parameter_id of this LogAnalyticsParserFunctionParameter.
        :type: int
        """
        self._parser_function_parameter_id = parser_function_parameter_id

    @property
    def parser_meta_plugin_parameter_name(self):
        """
        Gets the parser_meta_plugin_parameter_name of this LogAnalyticsParserFunctionParameter.
        The parameter internal name.


        :return: The parser_meta_plugin_parameter_name of this LogAnalyticsParserFunctionParameter.
        :rtype: str
        """
        return self._parser_meta_plugin_parameter_name

    @parser_meta_plugin_parameter_name.setter
    def parser_meta_plugin_parameter_name(self, parser_meta_plugin_parameter_name):
        """
        Sets the parser_meta_plugin_parameter_name of this LogAnalyticsParserFunctionParameter.
        The parameter internal name.


        :param parser_meta_plugin_parameter_name: The parser_meta_plugin_parameter_name of this LogAnalyticsParserFunctionParameter.
        :type: str
        """
        self._parser_meta_plugin_parameter_name = parser_meta_plugin_parameter_name

    @property
    def parser_meta_plugin_parameter_value(self):
        """
        Gets the parser_meta_plugin_parameter_value of this LogAnalyticsParserFunctionParameter.
        The parameter value.


        :return: The parser_meta_plugin_parameter_value of this LogAnalyticsParserFunctionParameter.
        :rtype: str
        """
        return self._parser_meta_plugin_parameter_value

    @parser_meta_plugin_parameter_value.setter
    def parser_meta_plugin_parameter_value(self, parser_meta_plugin_parameter_value):
        """
        Sets the parser_meta_plugin_parameter_value of this LogAnalyticsParserFunctionParameter.
        The parameter value.


        :param parser_meta_plugin_parameter_value: The parser_meta_plugin_parameter_value of this LogAnalyticsParserFunctionParameter.
        :type: str
        """
        self._parser_meta_plugin_parameter_value = parser_meta_plugin_parameter_value

    @property
    def parser_name(self):
        """
        Gets the parser_name of this LogAnalyticsParserFunctionParameter.
        The parser internal name.


        :return: The parser_name of this LogAnalyticsParserFunctionParameter.
        :rtype: str
        """
        return self._parser_name

    @parser_name.setter
    def parser_name(self, parser_name):
        """
        Sets the parser_name of this LogAnalyticsParserFunctionParameter.
        The parser internal name.


        :param parser_name: The parser_name of this LogAnalyticsParserFunctionParameter.
        :type: str
        """
        self._parser_name = parser_name

    @property
    def parser_meta_plugin_parameter(self):
        """
        Gets the parser_meta_plugin_parameter of this LogAnalyticsParserFunctionParameter.

        :return: The parser_meta_plugin_parameter of this LogAnalyticsParserFunctionParameter.
        :rtype: oci.log_analytics.models.LogAnalyticsParserMetaPluginParameter
        """
        return self._parser_meta_plugin_parameter

    @parser_meta_plugin_parameter.setter
    def parser_meta_plugin_parameter(self, parser_meta_plugin_parameter):
        """
        Sets the parser_meta_plugin_parameter of this LogAnalyticsParserFunctionParameter.

        :param parser_meta_plugin_parameter: The parser_meta_plugin_parameter of this LogAnalyticsParserFunctionParameter.
        :type: oci.log_analytics.models.LogAnalyticsParserMetaPluginParameter
        """
        self._parser_meta_plugin_parameter = parser_meta_plugin_parameter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
