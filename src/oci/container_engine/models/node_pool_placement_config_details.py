# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodePoolPlacementConfigDetails(object):
    """
    The location where a node pool will place nodes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodePoolPlacementConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this NodePoolPlacementConfigDetails.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this NodePoolPlacementConfigDetails.
        :type subnet_id: str

        :param capacity_reservation_id:
            The value to assign to the capacity_reservation_id property of this NodePoolPlacementConfigDetails.
        :type capacity_reservation_id: str

        :param fault_domains:
            The value to assign to the fault_domains property of this NodePoolPlacementConfigDetails.
        :type fault_domains: list[str]

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'subnet_id': 'str',
            'capacity_reservation_id': 'str',
            'fault_domains': 'list[str]'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'capacity_reservation_id': 'capacityReservationId',
            'fault_domains': 'faultDomains'
        }

        self._availability_domain = None
        self._subnet_id = None
        self._capacity_reservation_id = None
        self._fault_domains = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this NodePoolPlacementConfigDetails.
        The availability domain in which to place nodes.
        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this NodePoolPlacementConfigDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this NodePoolPlacementConfigDetails.
        The availability domain in which to place nodes.
        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this NodePoolPlacementConfigDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this NodePoolPlacementConfigDetails.
        The OCID of the subnet in which to place nodes.


        :return: The subnet_id of this NodePoolPlacementConfigDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this NodePoolPlacementConfigDetails.
        The OCID of the subnet in which to place nodes.


        :param subnet_id: The subnet_id of this NodePoolPlacementConfigDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def capacity_reservation_id(self):
        """
        Gets the capacity_reservation_id of this NodePoolPlacementConfigDetails.
        The OCID of the compute capacity reservation in which to place the compute instance.


        :return: The capacity_reservation_id of this NodePoolPlacementConfigDetails.
        :rtype: str
        """
        return self._capacity_reservation_id

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, capacity_reservation_id):
        """
        Sets the capacity_reservation_id of this NodePoolPlacementConfigDetails.
        The OCID of the compute capacity reservation in which to place the compute instance.


        :param capacity_reservation_id: The capacity_reservation_id of this NodePoolPlacementConfigDetails.
        :type: str
        """
        self._capacity_reservation_id = capacity_reservation_id

    @property
    def fault_domains(self):
        """
        Gets the fault_domains of this NodePoolPlacementConfigDetails.
        A list of fault domains in which to place nodes.


        :return: The fault_domains of this NodePoolPlacementConfigDetails.
        :rtype: list[str]
        """
        return self._fault_domains

    @fault_domains.setter
    def fault_domains(self, fault_domains):
        """
        Sets the fault_domains of this NodePoolPlacementConfigDetails.
        A list of fault domains in which to place nodes.


        :param fault_domains: The fault_domains of this NodePoolPlacementConfigDetails.
        :type: list[str]
        """
        self._fault_domains = fault_domains

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other