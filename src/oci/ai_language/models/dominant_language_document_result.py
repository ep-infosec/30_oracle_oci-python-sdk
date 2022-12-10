# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DominantLanguageDocumentResult(object):
    """
    The document response for language detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DominantLanguageDocumentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DominantLanguageDocumentResult.
        :type key: str

        :param languages:
            The value to assign to the languages property of this DominantLanguageDocumentResult.
        :type languages: list[oci.ai_language.models.DetectedLanguage]

        """
        self.swagger_types = {
            'key': 'str',
            'languages': 'list[DetectedLanguage]'
        }

        self.attribute_map = {
            'key': 'key',
            'languages': 'languages'
        }

        self._key = None
        self._languages = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DominantLanguageDocumentResult.
        Document unique identifier defined by the user.


        :return: The key of this DominantLanguageDocumentResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DominantLanguageDocumentResult.
        Document unique identifier defined by the user.


        :param key: The key of this DominantLanguageDocumentResult.
        :type: str
        """
        self._key = key

    @property
    def languages(self):
        """
        **[Required]** Gets the languages of this DominantLanguageDocumentResult.
        List of detected languages with results sorted in descending order of the scores. Most likely language is on top.


        :return: The languages of this DominantLanguageDocumentResult.
        :rtype: list[oci.ai_language.models.DetectedLanguage]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this DominantLanguageDocumentResult.
        List of detected languages with results sorted in descending order of the scores. Most likely language is on top.


        :param languages: The languages of this DominantLanguageDocumentResult.
        :type: list[oci.ai_language.models.DetectedLanguage]
        """
        self._languages = languages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
