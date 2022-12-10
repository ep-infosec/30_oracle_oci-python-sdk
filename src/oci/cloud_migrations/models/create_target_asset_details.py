# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTargetAssetDetails(object):
    """
    Details of the new target asset.
    """

    #: A constant which can be used with the type property of a CreateTargetAssetDetails.
    #: This constant has a value of "INSTANCE"
    TYPE_INSTANCE = "INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTargetAssetDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cloud_migrations.models.CreateVmTargetAssetDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param migration_plan_id:
            The value to assign to the migration_plan_id property of this CreateTargetAssetDetails.
        :type migration_plan_id: str

        :param type:
            The value to assign to the type property of this CreateTargetAssetDetails.
            Allowed values for this property are: "INSTANCE"
        :type type: str

        :param is_excluded_from_execution:
            The value to assign to the is_excluded_from_execution property of this CreateTargetAssetDetails.
        :type is_excluded_from_execution: bool

        """
        self.swagger_types = {
            'migration_plan_id': 'str',
            'type': 'str',
            'is_excluded_from_execution': 'bool'
        }

        self.attribute_map = {
            'migration_plan_id': 'migrationPlanId',
            'type': 'type',
            'is_excluded_from_execution': 'isExcludedFromExecution'
        }

        self._migration_plan_id = None
        self._type = None
        self._is_excluded_from_execution = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'INSTANCE':
            return 'CreateVmTargetAssetDetails'
        else:
            return 'CreateTargetAssetDetails'

    @property
    def migration_plan_id(self):
        """
        **[Required]** Gets the migration_plan_id of this CreateTargetAssetDetails.
        OCID of the associated migration plan.


        :return: The migration_plan_id of this CreateTargetAssetDetails.
        :rtype: str
        """
        return self._migration_plan_id

    @migration_plan_id.setter
    def migration_plan_id(self, migration_plan_id):
        """
        Sets the migration_plan_id of this CreateTargetAssetDetails.
        OCID of the associated migration plan.


        :param migration_plan_id: The migration_plan_id of this CreateTargetAssetDetails.
        :type: str
        """
        self._migration_plan_id = migration_plan_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateTargetAssetDetails.
        The type of target asset.

        Allowed values for this property are: "INSTANCE"


        :return: The type of this CreateTargetAssetDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateTargetAssetDetails.
        The type of target asset.


        :param type: The type of this CreateTargetAssetDetails.
        :type: str
        """
        allowed_values = ["INSTANCE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def is_excluded_from_execution(self):
        """
        **[Required]** Gets the is_excluded_from_execution of this CreateTargetAssetDetails.
        A boolean indicating whether the asset should be migrated.


        :return: The is_excluded_from_execution of this CreateTargetAssetDetails.
        :rtype: bool
        """
        return self._is_excluded_from_execution

    @is_excluded_from_execution.setter
    def is_excluded_from_execution(self, is_excluded_from_execution):
        """
        Sets the is_excluded_from_execution of this CreateTargetAssetDetails.
        A boolean indicating whether the asset should be migrated.


        :param is_excluded_from_execution: The is_excluded_from_execution of this CreateTargetAssetDetails.
        :type: bool
        """
        self._is_excluded_from_execution = is_excluded_from_execution

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
