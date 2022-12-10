# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_dr_plan_user_defined_step_details import UpdateDrPlanUserDefinedStepDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateObjectStoreScriptPrecheckStepDetails(UpdateDrPlanUserDefinedStepDetails):
    """
    The details for updating Run object store script precheck step.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateObjectStoreScriptPrecheckStepDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.UpdateObjectStoreScriptPrecheckStepDetails.step_type` attribute
        of this class is ``RUN_OBJECTSTORE_SCRIPT_PRECHECK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this UpdateObjectStoreScriptPrecheckStepDetails.
            Allowed values for this property are: "RUN_OBJECTSTORE_SCRIPT_PRECHECK", "RUN_LOCAL_SCRIPT_PRECHECK", "INVOKE_FUNCTION_PRECHECK", "RUN_OBJECTSTORE_SCRIPT", "RUN_LOCAL_SCRIPT", "INVOKE_FUNCTION"
        :type step_type: str

        """
        self.swagger_types = {
            'step_type': 'str'
        }

        self.attribute_map = {
            'step_type': 'stepType'
        }

        self._step_type = None
        self._step_type = 'RUN_OBJECTSTORE_SCRIPT_PRECHECK'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
