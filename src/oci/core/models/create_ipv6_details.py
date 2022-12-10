# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIpv6Details(object):
    """
    CreateIpv6Details model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIpv6Details object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIpv6Details.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateIpv6Details.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIpv6Details.
        :type freeform_tags: dict(str, str)

        :param ip_address:
            The value to assign to the ip_address property of this CreateIpv6Details.
        :type ip_address: str

        :param vnic_id:
            The value to assign to the vnic_id property of this CreateIpv6Details.
        :type vnic_id: str

        :param ipv6_subnet_cidr:
            The value to assign to the ipv6_subnet_cidr property of this CreateIpv6Details.
        :type ipv6_subnet_cidr: str

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'ip_address': 'str',
            'vnic_id': 'str',
            'ipv6_subnet_cidr': 'str'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'ip_address': 'ipAddress',
            'vnic_id': 'vnicId',
            'ipv6_subnet_cidr': 'ipv6SubnetCidr'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._ip_address = None
        self._vnic_id = None
        self._ipv6_subnet_cidr = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateIpv6Details.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateIpv6Details.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateIpv6Details.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateIpv6Details.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateIpv6Details.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateIpv6Details.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateIpv6Details.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateIpv6Details.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateIpv6Details.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateIpv6Details.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateIpv6Details.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateIpv6Details.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateIpv6Details.
        An IPv6 address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns an IPv6 address from the subnet. The subnet is the one that
        contains the VNIC you specify in `vnicId`.

        Example: `2001:DB8::`


        :return: The ip_address of this CreateIpv6Details.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateIpv6Details.
        An IPv6 address of your choice. Must be an available IP address within
        the subnet's CIDR. If you don't specify a value, Oracle automatically
        assigns an IPv6 address from the subnet. The subnet is the one that
        contains the VNIC you specify in `vnicId`.

        Example: `2001:DB8::`


        :param ip_address: The ip_address of this CreateIpv6Details.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def vnic_id(self):
        """
        **[Required]** Gets the vnic_id of this CreateIpv6Details.
        The `OCID`__ of the VNIC to assign the IPv6 to. The
        IPv6 will be in the VNIC's subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vnic_id of this CreateIpv6Details.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this CreateIpv6Details.
        The `OCID`__ of the VNIC to assign the IPv6 to. The
        IPv6 will be in the VNIC's subnet.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vnic_id: The vnic_id of this CreateIpv6Details.
        :type: str
        """
        self._vnic_id = vnic_id

    @property
    def ipv6_subnet_cidr(self):
        """
        Gets the ipv6_subnet_cidr of this CreateIpv6Details.
        The IPv6 CIDR allocated to the subnet. This is required if more than one IPv6 CIDR exists on the subnet.


        :return: The ipv6_subnet_cidr of this CreateIpv6Details.
        :rtype: str
        """
        return self._ipv6_subnet_cidr

    @ipv6_subnet_cidr.setter
    def ipv6_subnet_cidr(self, ipv6_subnet_cidr):
        """
        Sets the ipv6_subnet_cidr of this CreateIpv6Details.
        The IPv6 CIDR allocated to the subnet. This is required if more than one IPv6 CIDR exists on the subnet.


        :param ipv6_subnet_cidr: The ipv6_subnet_cidr of this CreateIpv6Details.
        :type: str
        """
        self._ipv6_subnet_cidr = ipv6_subnet_cidr

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other