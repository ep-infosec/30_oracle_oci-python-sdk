# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .volume_group_source_details import VolumeGroupSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupSourceFromVolumeGroupReplicaDetails(VolumeGroupSourceDetails):
    """
    Specifies the source volume replica which the volume group will be created from.
    The volume group replica shoulbe be in the same availability domain as the volume group.
    Only one volume group can be created from a volume group replica at the same time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupSourceFromVolumeGroupReplicaDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VolumeGroupSourceFromVolumeGroupReplicaDetails.type` attribute
        of this class is ``volumeGroupReplicaId`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VolumeGroupSourceFromVolumeGroupReplicaDetails.
        :type type: str

        :param volume_group_replica_id:
            The value to assign to the volume_group_replica_id property of this VolumeGroupSourceFromVolumeGroupReplicaDetails.
        :type volume_group_replica_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'volume_group_replica_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'volume_group_replica_id': 'volumeGroupReplicaId'
        }

        self._type = None
        self._volume_group_replica_id = None
        self._type = 'volumeGroupReplicaId'

    @property
    def volume_group_replica_id(self):
        """
        **[Required]** Gets the volume_group_replica_id of this VolumeGroupSourceFromVolumeGroupReplicaDetails.
        The OCID of the volume group replica.


        :return: The volume_group_replica_id of this VolumeGroupSourceFromVolumeGroupReplicaDetails.
        :rtype: str
        """
        return self._volume_group_replica_id

    @volume_group_replica_id.setter
    def volume_group_replica_id(self, volume_group_replica_id):
        """
        Sets the volume_group_replica_id of this VolumeGroupSourceFromVolumeGroupReplicaDetails.
        The OCID of the volume group replica.


        :param volume_group_replica_id: The volume_group_replica_id of this VolumeGroupSourceFromVolumeGroupReplicaDetails.
        :type: str
        """
        self._volume_group_replica_id = volume_group_replica_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
