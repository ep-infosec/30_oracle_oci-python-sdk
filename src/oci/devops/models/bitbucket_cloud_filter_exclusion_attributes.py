# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BitbucketCloudFilterExclusionAttributes(object):
    """
    Attributes to filter Bitbucket Cloud events. File filter criteria - Changes only affecting excluded files will not invoke a build. if both include and exclude filter are used then exclusion filter will be applied on the result set of inclusion filter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BitbucketCloudFilterExclusionAttributes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_filter:
            The value to assign to the file_filter property of this BitbucketCloudFilterExclusionAttributes.
        :type file_filter: oci.devops.models.FileFilter

        """
        self.swagger_types = {
            'file_filter': 'FileFilter'
        }

        self.attribute_map = {
            'file_filter': 'fileFilter'
        }

        self._file_filter = None

    @property
    def file_filter(self):
        """
        Gets the file_filter of this BitbucketCloudFilterExclusionAttributes.

        :return: The file_filter of this BitbucketCloudFilterExclusionAttributes.
        :rtype: oci.devops.models.FileFilter
        """
        return self._file_filter

    @file_filter.setter
    def file_filter(self, file_filter):
        """
        Sets the file_filter of this BitbucketCloudFilterExclusionAttributes.

        :param file_filter: The file_filter of this BitbucketCloudFilterExclusionAttributes.
        :type: oci.devops.models.FileFilter
        """
        self._file_filter = file_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
