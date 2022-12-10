# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .traffic_node import TrafficNode
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessDeniedTrafficNode(TrafficNode):
    """
    Defines the configuration of a traffic node to which the user is denied access.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessDeniedTrafficNode object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.AccessDeniedTrafficNode.type` attribute
        of this class is ``ACCESS_DENIED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AccessDeniedTrafficNode.
            Allowed values for this property are: "VISIBLE", "ACCESS_DENIED"
        :type type: str

        :param egress_traffic:
            The value to assign to the egress_traffic property of this AccessDeniedTrafficNode.
        :type egress_traffic: oci.vn_monitoring.models.EgressTrafficSpec

        :param next_hop_routing_action:
            The value to assign to the next_hop_routing_action property of this AccessDeniedTrafficNode.
        :type next_hop_routing_action: oci.vn_monitoring.models.RoutingAction

        :param egress_security_action:
            The value to assign to the egress_security_action property of this AccessDeniedTrafficNode.
        :type egress_security_action: oci.vn_monitoring.models.SecurityAction

        :param ingress_security_action:
            The value to assign to the ingress_security_action property of this AccessDeniedTrafficNode.
        :type ingress_security_action: oci.vn_monitoring.models.SecurityAction

        """
        self.swagger_types = {
            'type': 'str',
            'egress_traffic': 'EgressTrafficSpec',
            'next_hop_routing_action': 'RoutingAction',
            'egress_security_action': 'SecurityAction',
            'ingress_security_action': 'SecurityAction'
        }

        self.attribute_map = {
            'type': 'type',
            'egress_traffic': 'egressTraffic',
            'next_hop_routing_action': 'nextHopRoutingAction',
            'egress_security_action': 'egressSecurityAction',
            'ingress_security_action': 'ingressSecurityAction'
        }

        self._type = None
        self._egress_traffic = None
        self._next_hop_routing_action = None
        self._egress_security_action = None
        self._ingress_security_action = None
        self._type = 'ACCESS_DENIED'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
