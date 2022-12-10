# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Suppression(object):
    """
    The configuration details for suppressing an alarm.
    For information about alarms, see `Alarms Overview`__.

    __ https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#AlarmsOverview
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Suppression object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this Suppression.
        :type description: str

        :param time_suppress_from:
            The value to assign to the time_suppress_from property of this Suppression.
        :type time_suppress_from: datetime

        :param time_suppress_until:
            The value to assign to the time_suppress_until property of this Suppression.
        :type time_suppress_until: datetime

        """
        self.swagger_types = {
            'description': 'str',
            'time_suppress_from': 'datetime',
            'time_suppress_until': 'datetime'
        }

        self.attribute_map = {
            'description': 'description',
            'time_suppress_from': 'timeSuppressFrom',
            'time_suppress_until': 'timeSuppressUntil'
        }

        self._description = None
        self._time_suppress_from = None
        self._time_suppress_until = None

    @property
    def description(self):
        """
        Gets the description of this Suppression.
        Human-readable reason for suppressing alarm notifications.
        It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Oracle recommends including tracking information for the event or associated work,
        such as a ticket number.

        Example: `Planned outage due to change IT-1234.`


        :return: The description of this Suppression.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Suppression.
        Human-readable reason for suppressing alarm notifications.
        It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Oracle recommends including tracking information for the event or associated work,
        such as a ticket number.

        Example: `Planned outage due to change IT-1234.`


        :param description: The description of this Suppression.
        :type: str
        """
        self._description = description

    @property
    def time_suppress_from(self):
        """
        **[Required]** Gets the time_suppress_from of this Suppression.
        The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.

        Example: `2019-02-01T01:02:29.600Z`


        :return: The time_suppress_from of this Suppression.
        :rtype: datetime
        """
        return self._time_suppress_from

    @time_suppress_from.setter
    def time_suppress_from(self, time_suppress_from):
        """
        Sets the time_suppress_from of this Suppression.
        The start date and time for the suppression to take place, inclusive. Format defined by RFC3339.

        Example: `2019-02-01T01:02:29.600Z`


        :param time_suppress_from: The time_suppress_from of this Suppression.
        :type: datetime
        """
        self._time_suppress_from = time_suppress_from

    @property
    def time_suppress_until(self):
        """
        **[Required]** Gets the time_suppress_until of this Suppression.
        The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.

        Example: `2019-02-01T02:02:29.600Z`


        :return: The time_suppress_until of this Suppression.
        :rtype: datetime
        """
        return self._time_suppress_until

    @time_suppress_until.setter
    def time_suppress_until(self, time_suppress_until):
        """
        Sets the time_suppress_until of this Suppression.
        The end date and time for the suppression to take place, inclusive. Format defined by RFC3339.

        Example: `2019-02-01T02:02:29.600Z`


        :param time_suppress_until: The time_suppress_until of this Suppression.
        :type: datetime
        """
        self._time_suppress_until = time_suppress_until

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
