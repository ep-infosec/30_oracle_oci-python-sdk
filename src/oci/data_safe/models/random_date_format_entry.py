# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .format_entry import FormatEntry
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RandomDateFormatEntry(FormatEntry):
    """
    The Random Date masking format generates random and unique dates within a range.
    The date range is defined by the startDate and endDate attributes. The start date
    must be less than or equal to the end date. When masking columns with uniqueness
    constraint, ensure that the date range is sufficient enough to generate unique
    values. To learn more, check Random Date in the Data Safe documentation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RandomDateFormatEntry object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.RandomDateFormatEntry.type` attribute
        of this class is ``RANDOM_DATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RandomDateFormatEntry.
            Allowed values for this property are: "DELETE_ROWS", "DETERMINISTIC_SUBSTITUTION", "DETERMINISTIC_ENCRYPTION", "DETERMINISTIC_ENCRYPTION_DATE", "FIXED_NUMBER", "FIXED_STRING", "LIBRARY_MASKING_FORMAT", "NULL_VALUE", "POST_PROCESSING_FUNCTION", "PRESERVE_ORIGINAL_DATA", "RANDOM_DATE", "RANDOM_DECIMAL_NUMBER", "RANDOM_DIGITS", "RANDOM_LIST", "RANDOM_NUMBER", "RANDOM_STRING", "RANDOM_SUBSTITUTION", "REGULAR_EXPRESSION", "SHUFFLE", "SQL_EXPRESSION", "SUBSTRING", "TRUNCATE_TABLE", "USER_DEFINED_FUNCTION"
        :type type: str

        :param description:
            The value to assign to the description property of this RandomDateFormatEntry.
        :type description: str

        :param start_date:
            The value to assign to the start_date property of this RandomDateFormatEntry.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this RandomDateFormatEntry.
        :type end_date: datetime

        """
        self.swagger_types = {
            'type': 'str',
            'description': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime'
        }

        self.attribute_map = {
            'type': 'type',
            'description': 'description',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }

        self._type = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._type = 'RANDOM_DATE'

    @property
    def start_date(self):
        """
        **[Required]** Gets the start_date of this RandomDateFormatEntry.
        The lower bound of the range within which random dates should be generated.
        The start date must be less than or equal to the end date.


        :return: The start_date of this RandomDateFormatEntry.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this RandomDateFormatEntry.
        The lower bound of the range within which random dates should be generated.
        The start date must be less than or equal to the end date.


        :param start_date: The start_date of this RandomDateFormatEntry.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        **[Required]** Gets the end_date of this RandomDateFormatEntry.
        The upper bound of the range within which random dates should be generated.
        The end date must be greater than or equal to the start date.


        :return: The end_date of this RandomDateFormatEntry.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this RandomDateFormatEntry.
        The upper bound of the range within which random dates should be generated.
        The end date must be greater than or equal to the start date.


        :param end_date: The end_date of this RandomDateFormatEntry.
        :type: datetime
        """
        self._end_date = end_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
