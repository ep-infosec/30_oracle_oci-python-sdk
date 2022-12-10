# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_deployment_details import CreateDeploymentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeployPipelineDeploymentDetails(CreateDeploymentDetails):
    """
    Details of the new deployment to be created that will run all the stages in the pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeployPipelineDeploymentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.CreateDeployPipelineDeploymentDetails.deployment_type` attribute
        of this class is ``PIPELINE_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateDeployPipelineDeploymentDetails.
        :type deploy_pipeline_id: str

        :param deployment_type:
            The value to assign to the deployment_type property of this CreateDeployPipelineDeploymentDetails.
        :type deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateDeployPipelineDeploymentDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeployPipelineDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeployPipelineDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param deployment_arguments:
            The value to assign to the deployment_arguments property of this CreateDeployPipelineDeploymentDetails.
        :type deployment_arguments: oci.devops.models.DeploymentArgumentCollection

        :param deploy_stage_override_arguments:
            The value to assign to the deploy_stage_override_arguments property of this CreateDeployPipelineDeploymentDetails.
        :type deploy_stage_override_arguments: oci.devops.models.DeployStageOverrideArgumentCollection

        :param deploy_artifact_override_arguments:
            The value to assign to the deploy_artifact_override_arguments property of this CreateDeployPipelineDeploymentDetails.
        :type deploy_artifact_override_arguments: oci.devops.models.DeployArtifactOverrideArgumentCollection

        """
        self.swagger_types = {
            'deploy_pipeline_id': 'str',
            'deployment_type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'deployment_arguments': 'DeploymentArgumentCollection',
            'deploy_stage_override_arguments': 'DeployStageOverrideArgumentCollection',
            'deploy_artifact_override_arguments': 'DeployArtifactOverrideArgumentCollection'
        }

        self.attribute_map = {
            'deploy_pipeline_id': 'deployPipelineId',
            'deployment_type': 'deploymentType',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'deployment_arguments': 'deploymentArguments',
            'deploy_stage_override_arguments': 'deployStageOverrideArguments',
            'deploy_artifact_override_arguments': 'deployArtifactOverrideArguments'
        }

        self._deploy_pipeline_id = None
        self._deployment_type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._deployment_arguments = None
        self._deploy_stage_override_arguments = None
        self._deploy_artifact_override_arguments = None
        self._deployment_type = 'PIPELINE_DEPLOYMENT'

    @property
    def deployment_arguments(self):
        """
        Gets the deployment_arguments of this CreateDeployPipelineDeploymentDetails.

        :return: The deployment_arguments of this CreateDeployPipelineDeploymentDetails.
        :rtype: oci.devops.models.DeploymentArgumentCollection
        """
        return self._deployment_arguments

    @deployment_arguments.setter
    def deployment_arguments(self, deployment_arguments):
        """
        Sets the deployment_arguments of this CreateDeployPipelineDeploymentDetails.

        :param deployment_arguments: The deployment_arguments of this CreateDeployPipelineDeploymentDetails.
        :type: oci.devops.models.DeploymentArgumentCollection
        """
        self._deployment_arguments = deployment_arguments

    @property
    def deploy_stage_override_arguments(self):
        """
        Gets the deploy_stage_override_arguments of this CreateDeployPipelineDeploymentDetails.

        :return: The deploy_stage_override_arguments of this CreateDeployPipelineDeploymentDetails.
        :rtype: oci.devops.models.DeployStageOverrideArgumentCollection
        """
        return self._deploy_stage_override_arguments

    @deploy_stage_override_arguments.setter
    def deploy_stage_override_arguments(self, deploy_stage_override_arguments):
        """
        Sets the deploy_stage_override_arguments of this CreateDeployPipelineDeploymentDetails.

        :param deploy_stage_override_arguments: The deploy_stage_override_arguments of this CreateDeployPipelineDeploymentDetails.
        :type: oci.devops.models.DeployStageOverrideArgumentCollection
        """
        self._deploy_stage_override_arguments = deploy_stage_override_arguments

    @property
    def deploy_artifact_override_arguments(self):
        """
        Gets the deploy_artifact_override_arguments of this CreateDeployPipelineDeploymentDetails.

        :return: The deploy_artifact_override_arguments of this CreateDeployPipelineDeploymentDetails.
        :rtype: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        return self._deploy_artifact_override_arguments

    @deploy_artifact_override_arguments.setter
    def deploy_artifact_override_arguments(self, deploy_artifact_override_arguments):
        """
        Sets the deploy_artifact_override_arguments of this CreateDeployPipelineDeploymentDetails.

        :param deploy_artifact_override_arguments: The deploy_artifact_override_arguments of this CreateDeployPipelineDeploymentDetails.
        :type: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        self._deploy_artifact_override_arguments = deploy_artifact_override_arguments

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
