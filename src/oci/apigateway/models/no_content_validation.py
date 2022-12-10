# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .content_validation import ContentValidation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NoContentValidation(ContentValidation):
    """
    No content validation properties.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NoContentValidation object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.NoContentValidation.validation_type` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param validation_type:
            The value to assign to the validation_type property of this NoContentValidation.
            Allowed values for this property are: "NONE"
        :type validation_type: str

        """
        self.swagger_types = {
            'validation_type': 'str'
        }

        self.attribute_map = {
            'validation_type': 'validationType'
        }

        self._validation_type = None
        self._validation_type = 'NONE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other