# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkPolicy(object):
    """
    Network policy, which consists of a list of network source IDs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_source_ids:
            The value to assign to the network_source_ids property of this NetworkPolicy.
        :type network_source_ids: list[str]

        """
        self.swagger_types = {
            'network_source_ids': 'list[str]'
        }

        self.attribute_map = {
            'network_source_ids': 'networkSourceIds'
        }

        self._network_source_ids = None

    @property
    def network_source_ids(self):
        """
        Gets the network_source_ids of this NetworkPolicy.
        Network Source ids


        :return: The network_source_ids of this NetworkPolicy.
        :rtype: list[str]
        """
        return self._network_source_ids

    @network_source_ids.setter
    def network_source_ids(self, network_source_ids):
        """
        Sets the network_source_ids of this NetworkPolicy.
        Network Source ids


        :param network_source_ids: The network_source_ids of this NetworkPolicy.
        :type: list[str]
        """
        self._network_source_ids = network_source_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other