# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsParserField(object):
    """
    LogAnalyticsParserField
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsParserField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field:
            The value to assign to the field property of this LogAnalyticsParserField.
        :type field: oci.log_analytics.models.LogAnalyticsField

        :param parser_field_id:
            The value to assign to the parser_field_id property of this LogAnalyticsParserField.
        :type parser_field_id: int

        :param parser_field_expression:
            The value to assign to the parser_field_expression property of this LogAnalyticsParserField.
        :type parser_field_expression: str

        :param parser_field_name:
            The value to assign to the parser_field_name property of this LogAnalyticsParserField.
        :type parser_field_name: str

        :param storage_field_name:
            The value to assign to the storage_field_name property of this LogAnalyticsParserField.
        :type storage_field_name: str

        :param parser_field_integrator_name:
            The value to assign to the parser_field_integrator_name property of this LogAnalyticsParserField.
        :type parser_field_integrator_name: str

        :param parser_name:
            The value to assign to the parser_name property of this LogAnalyticsParserField.
        :type parser_name: str

        :param parser_field_sequence:
            The value to assign to the parser_field_sequence property of this LogAnalyticsParserField.
        :type parser_field_sequence: int

        :param parser:
            The value to assign to the parser property of this LogAnalyticsParserField.
        :type parser: oci.log_analytics.models.LogAnalyticsParser

        :param structured_column_info:
            The value to assign to the structured_column_info property of this LogAnalyticsParserField.
        :type structured_column_info: str

        """
        self.swagger_types = {
            'field': 'LogAnalyticsField',
            'parser_field_id': 'int',
            'parser_field_expression': 'str',
            'parser_field_name': 'str',
            'storage_field_name': 'str',
            'parser_field_integrator_name': 'str',
            'parser_name': 'str',
            'parser_field_sequence': 'int',
            'parser': 'LogAnalyticsParser',
            'structured_column_info': 'str'
        }

        self.attribute_map = {
            'field': 'field',
            'parser_field_id': 'parserFieldId',
            'parser_field_expression': 'parserFieldExpression',
            'parser_field_name': 'parserFieldName',
            'storage_field_name': 'storageFieldName',
            'parser_field_integrator_name': 'parserFieldIntegratorName',
            'parser_name': 'parserName',
            'parser_field_sequence': 'parserFieldSequence',
            'parser': 'parser',
            'structured_column_info': 'structuredColumnInfo'
        }

        self._field = None
        self._parser_field_id = None
        self._parser_field_expression = None
        self._parser_field_name = None
        self._storage_field_name = None
        self._parser_field_integrator_name = None
        self._parser_name = None
        self._parser_field_sequence = None
        self._parser = None
        self._structured_column_info = None

    @property
    def field(self):
        """
        Gets the field of this LogAnalyticsParserField.

        :return: The field of this LogAnalyticsParserField.
        :rtype: oci.log_analytics.models.LogAnalyticsField
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this LogAnalyticsParserField.

        :param field: The field of this LogAnalyticsParserField.
        :type: oci.log_analytics.models.LogAnalyticsField
        """
        self._field = field

    @property
    def parser_field_id(self):
        """
        Gets the parser_field_id of this LogAnalyticsParserField.
        The parser field unique identifier.


        :return: The parser_field_id of this LogAnalyticsParserField.
        :rtype: int
        """
        return self._parser_field_id

    @parser_field_id.setter
    def parser_field_id(self, parser_field_id):
        """
        Sets the parser_field_id of this LogAnalyticsParserField.
        The parser field unique identifier.


        :param parser_field_id: The parser_field_id of this LogAnalyticsParserField.
        :type: int
        """
        self._parser_field_id = parser_field_id

    @property
    def parser_field_expression(self):
        """
        Gets the parser_field_expression of this LogAnalyticsParserField.
        the parser field expression.


        :return: The parser_field_expression of this LogAnalyticsParserField.
        :rtype: str
        """
        return self._parser_field_expression

    @parser_field_expression.setter
    def parser_field_expression(self, parser_field_expression):
        """
        Sets the parser_field_expression of this LogAnalyticsParserField.
        the parser field expression.


        :param parser_field_expression: The parser_field_expression of this LogAnalyticsParserField.
        :type: str
        """
        self._parser_field_expression = parser_field_expression

    @property
    def parser_field_name(self):
        """
        Gets the parser_field_name of this LogAnalyticsParserField.
        The parser field internal name.


        :return: The parser_field_name of this LogAnalyticsParserField.
        :rtype: str
        """
        return self._parser_field_name

    @parser_field_name.setter
    def parser_field_name(self, parser_field_name):
        """
        Sets the parser_field_name of this LogAnalyticsParserField.
        The parser field internal name.


        :param parser_field_name: The parser_field_name of this LogAnalyticsParserField.
        :type: str
        """
        self._parser_field_name = parser_field_name

    @property
    def storage_field_name(self):
        """
        Gets the storage_field_name of this LogAnalyticsParserField.
        The storage field name.


        :return: The storage_field_name of this LogAnalyticsParserField.
        :rtype: str
        """
        return self._storage_field_name

    @storage_field_name.setter
    def storage_field_name(self, storage_field_name):
        """
        Sets the storage_field_name of this LogAnalyticsParserField.
        The storage field name.


        :param storage_field_name: The storage_field_name of this LogAnalyticsParserField.
        :type: str
        """
        self._storage_field_name = storage_field_name

    @property
    def parser_field_integrator_name(self):
        """
        Gets the parser_field_integrator_name of this LogAnalyticsParserField.
        The integrator name.


        :return: The parser_field_integrator_name of this LogAnalyticsParserField.
        :rtype: str
        """
        return self._parser_field_integrator_name

    @parser_field_integrator_name.setter
    def parser_field_integrator_name(self, parser_field_integrator_name):
        """
        Sets the parser_field_integrator_name of this LogAnalyticsParserField.
        The integrator name.


        :param parser_field_integrator_name: The parser_field_integrator_name of this LogAnalyticsParserField.
        :type: str
        """
        self._parser_field_integrator_name = parser_field_integrator_name

    @property
    def parser_name(self):
        """
        Gets the parser_name of this LogAnalyticsParserField.
        The parser internal name.


        :return: The parser_name of this LogAnalyticsParserField.
        :rtype: str
        """
        return self._parser_name

    @parser_name.setter
    def parser_name(self, parser_name):
        """
        Sets the parser_name of this LogAnalyticsParserField.
        The parser internal name.


        :param parser_name: The parser_name of this LogAnalyticsParserField.
        :type: str
        """
        self._parser_name = parser_name

    @property
    def parser_field_sequence(self):
        """
        Gets the parser_field_sequence of this LogAnalyticsParserField.
        The parser field sequence.


        :return: The parser_field_sequence of this LogAnalyticsParserField.
        :rtype: int
        """
        return self._parser_field_sequence

    @parser_field_sequence.setter
    def parser_field_sequence(self, parser_field_sequence):
        """
        Sets the parser_field_sequence of this LogAnalyticsParserField.
        The parser field sequence.


        :param parser_field_sequence: The parser_field_sequence of this LogAnalyticsParserField.
        :type: int
        """
        self._parser_field_sequence = parser_field_sequence

    @property
    def parser(self):
        """
        Gets the parser of this LogAnalyticsParserField.

        :return: The parser of this LogAnalyticsParserField.
        :rtype: oci.log_analytics.models.LogAnalyticsParser
        """
        return self._parser

    @parser.setter
    def parser(self, parser):
        """
        Sets the parser of this LogAnalyticsParserField.

        :param parser: The parser of this LogAnalyticsParserField.
        :type: oci.log_analytics.models.LogAnalyticsParser
        """
        self._parser = parser

    @property
    def structured_column_info(self):
        """
        Gets the structured_column_info of this LogAnalyticsParserField.
        The structured column information.


        :return: The structured_column_info of this LogAnalyticsParserField.
        :rtype: str
        """
        return self._structured_column_info

    @structured_column_info.setter
    def structured_column_info(self, structured_column_info):
        """
        Sets the structured_column_info of this LogAnalyticsParserField.
        The structured column information.


        :param structured_column_info: The structured_column_info of this LogAnalyticsParserField.
        :type: str
        """
        self._structured_column_info = structured_column_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
