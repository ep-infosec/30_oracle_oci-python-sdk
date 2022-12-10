# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateIngressGatewayRouteTableDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateIngressGatewayRouteTableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateIngressGatewayRouteTableDetails.
        :type description: str

        :param priority:
            The value to assign to the priority property of this UpdateIngressGatewayRouteTableDetails.
        :type priority: int

        :param route_rules:
            The value to assign to the route_rules property of this UpdateIngressGatewayRouteTableDetails.
        :type route_rules: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateIngressGatewayRouteTableDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateIngressGatewayRouteTableDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'priority': 'int',
            'route_rules': 'list[IngressGatewayTrafficRouteRule]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'priority': 'priority',
            'route_rules': 'routeRules',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._priority = None
        self._route_rules = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this UpdateIngressGatewayRouteTableDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this UpdateIngressGatewayRouteTableDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateIngressGatewayRouteTableDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this UpdateIngressGatewayRouteTableDetails.
        :type: str
        """
        self._description = description

    @property
    def priority(self):
        """
        Gets the priority of this UpdateIngressGatewayRouteTableDetails.
        The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.


        :return: The priority of this UpdateIngressGatewayRouteTableDetails.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this UpdateIngressGatewayRouteTableDetails.
        The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.


        :param priority: The priority of this UpdateIngressGatewayRouteTableDetails.
        :type: int
        """
        self._priority = priority

    @property
    def route_rules(self):
        """
        Gets the route_rules of this UpdateIngressGatewayRouteTableDetails.
        The route rules for the ingress gateway.


        :return: The route_rules of this UpdateIngressGatewayRouteTableDetails.
        :rtype: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this UpdateIngressGatewayRouteTableDetails.
        The route rules for the ingress gateway.


        :param route_rules: The route_rules of this UpdateIngressGatewayRouteTableDetails.
        :type: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]
        """
        self._route_rules = route_rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateIngressGatewayRouteTableDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateIngressGatewayRouteTableDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateIngressGatewayRouteTableDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateIngressGatewayRouteTableDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateIngressGatewayRouteTableDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateIngressGatewayRouteTableDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateIngressGatewayRouteTableDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateIngressGatewayRouteTableDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
