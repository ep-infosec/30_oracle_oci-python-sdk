# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGatewayListener(object):
    """
    Listener configuration.
    """

    #: A constant which can be used with the protocol property of a IngressGatewayListener.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a IngressGatewayListener.
    #: This constant has a value of "TLS_PASSTHROUGH"
    PROTOCOL_TLS_PASSTHROUGH = "TLS_PASSTHROUGH"

    #: A constant which can be used with the protocol property of a IngressGatewayListener.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGatewayListener object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this IngressGatewayListener.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param port:
            The value to assign to the port property of this IngressGatewayListener.
        :type port: int

        :param tls:
            The value to assign to the tls property of this IngressGatewayListener.
        :type tls: oci.service_mesh.models.IngressListenerTlsConfig

        """
        self.swagger_types = {
            'protocol': 'str',
            'port': 'int',
            'tls': 'IngressListenerTlsConfig'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'port': 'port',
            'tls': 'tls'
        }

        self._protocol = None
        self._port = None
        self._tls = None

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this IngressGatewayListener.
        Type of protocol used.

        Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this IngressGatewayListener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this IngressGatewayListener.
        Type of protocol used.


        :param protocol: The protocol of this IngressGatewayListener.
        :type: str
        """
        allowed_values = ["HTTP", "TLS_PASSTHROUGH", "TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def port(self):
        """
        **[Required]** Gets the port of this IngressGatewayListener.
        Port on which ingress gateway is listening.


        :return: The port of this IngressGatewayListener.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this IngressGatewayListener.
        Port on which ingress gateway is listening.


        :param port: The port of this IngressGatewayListener.
        :type: int
        """
        self._port = port

    @property
    def tls(self):
        """
        Gets the tls of this IngressGatewayListener.

        :return: The tls of this IngressGatewayListener.
        :rtype: oci.service_mesh.models.IngressListenerTlsConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """
        Sets the tls of this IngressGatewayListener.

        :param tls: The tls of this IngressGatewayListener.
        :type: oci.service_mesh.models.IngressListenerTlsConfig
        """
        self._tls = tls

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
