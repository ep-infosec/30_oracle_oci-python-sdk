# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateQueryDetails(object):
    """
    Details for the query to update reportQuery, costAnalysisUI, and displayName.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateQueryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query_definition:
            The value to assign to the query_definition property of this UpdateQueryDetails.
        :type query_definition: oci.usage_api.models.QueryDefinition

        """
        self.swagger_types = {
            'query_definition': 'QueryDefinition'
        }

        self.attribute_map = {
            'query_definition': 'queryDefinition'
        }

        self._query_definition = None

    @property
    def query_definition(self):
        """
        **[Required]** Gets the query_definition of this UpdateQueryDetails.

        :return: The query_definition of this UpdateQueryDetails.
        :rtype: oci.usage_api.models.QueryDefinition
        """
        return self._query_definition

    @query_definition.setter
    def query_definition(self, query_definition):
        """
        Sets the query_definition of this UpdateQueryDetails.

        :param query_definition: The query_definition of this UpdateQueryDetails.
        :type: oci.usage_api.models.QueryDefinition
        """
        self._query_definition = query_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
