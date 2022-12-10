# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateReplicaDetails(object):
    """
    Details required to create a read replica.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateReplicaDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateReplicaDetails.
        :type db_system_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateReplicaDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateReplicaDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateReplicaDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateReplicaDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_delete_protected:
            The value to assign to the is_delete_protected property of this CreateReplicaDetails.
        :type is_delete_protected: bool

        """
        self.swagger_types = {
            'db_system_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_delete_protected': 'bool'
        }

        self.attribute_map = {
            'db_system_id': 'dbSystemId',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_delete_protected': 'isDeleteProtected'
        }

        self._db_system_id = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_delete_protected = None

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this CreateReplicaDetails.
        The OCID of the DB System the read replica is associated with.


        :return: The db_system_id of this CreateReplicaDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateReplicaDetails.
        The OCID of the DB System the read replica is associated with.


        :param db_system_id: The db_system_id of this CreateReplicaDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateReplicaDetails.
        The user-friendly name for the read replica. It does not have to be unique.


        :return: The display_name of this CreateReplicaDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateReplicaDetails.
        The user-friendly name for the read replica. It does not have to be unique.


        :param display_name: The display_name of this CreateReplicaDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateReplicaDetails.
        User provided description of the read replica.


        :return: The description of this CreateReplicaDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateReplicaDetails.
        User provided description of the read replica.


        :param description: The description of this CreateReplicaDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateReplicaDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateReplicaDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateReplicaDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateReplicaDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateReplicaDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateReplicaDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateReplicaDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateReplicaDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_delete_protected(self):
        """
        Gets the is_delete_protected of this CreateReplicaDetails.
        Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
        Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
        the DB System is delete protected, read replicas can still be deleted individually if they are not delete
        protected themselves.


        :return: The is_delete_protected of this CreateReplicaDetails.
        :rtype: bool
        """
        return self._is_delete_protected

    @is_delete_protected.setter
    def is_delete_protected(self, is_delete_protected):
        """
        Sets the is_delete_protected of this CreateReplicaDetails.
        Specifies whether the read replica can be deleted. Set to true to prevent deletion, false (default) to allow.
        Note that if a read replica is delete protected it also prevents the entire DB System from being deleted. If
        the DB System is delete protected, read replicas can still be deleted individually if they are not delete
        protected themselves.


        :param is_delete_protected: The is_delete_protected of this CreateReplicaDetails.
        :type: bool
        """
        self._is_delete_protected = is_delete_protected

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
