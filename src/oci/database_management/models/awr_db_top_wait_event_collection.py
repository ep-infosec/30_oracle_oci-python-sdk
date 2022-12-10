# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .awr_query_result import AwrQueryResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbTopWaitEventCollection(AwrQueryResult):
    """
    The AWR top wait event data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbTopWaitEventCollection object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.AwrDbTopWaitEventCollection.awr_result_type` attribute
        of this class is ``AWRDB_TOP_EVENT_SET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbTopWaitEventCollection.
        :type name: str

        :param version:
            The value to assign to the version property of this AwrDbTopWaitEventCollection.
        :type version: str

        :param query_key:
            The value to assign to the query_key property of this AwrDbTopWaitEventCollection.
        :type query_key: str

        :param db_query_time_in_secs:
            The value to assign to the db_query_time_in_secs property of this AwrDbTopWaitEventCollection.
        :type db_query_time_in_secs: float

        :param awr_result_type:
            The value to assign to the awr_result_type property of this AwrDbTopWaitEventCollection.
            Allowed values for this property are: "AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type awr_result_type: str

        :param items:
            The value to assign to the items property of this AwrDbTopWaitEventCollection.
        :type items: list[oci.database_management.models.AwrDbTopWaitEventSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'query_key': 'str',
            'db_query_time_in_secs': 'float',
            'awr_result_type': 'str',
            'items': 'list[AwrDbTopWaitEventSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'query_key': 'queryKey',
            'db_query_time_in_secs': 'dbQueryTimeInSecs',
            'awr_result_type': 'awrResultType',
            'items': 'items'
        }

        self._name = None
        self._version = None
        self._query_key = None
        self._db_query_time_in_secs = None
        self._awr_result_type = None
        self._items = None
        self._awr_result_type = 'AWRDB_TOP_EVENT_SET'

    @property
    def items(self):
        """
        Gets the items of this AwrDbTopWaitEventCollection.
        A list of AWR top event summary data.


        :return: The items of this AwrDbTopWaitEventCollection.
        :rtype: list[oci.database_management.models.AwrDbTopWaitEventSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AwrDbTopWaitEventCollection.
        A list of AWR top event summary data.


        :param items: The items of this AwrDbTopWaitEventCollection.
        :type: list[oci.database_management.models.AwrDbTopWaitEventSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
