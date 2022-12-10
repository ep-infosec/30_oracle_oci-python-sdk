# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_channel_details import UpdateChannelDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTwilioChannelDetails(UpdateChannelDetails):
    """
    Properties to update a Twilio channel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTwilioChannelDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.oda.models.UpdateTwilioChannelDetails.type` attribute
        of this class is ``TWILIO`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateTwilioChannelDetails.
        :type description: str

        :param type:
            The value to assign to the type property of this UpdateTwilioChannelDetails.
            Allowed values for this property are: "ANDROID", "APPEVENT", "APPLICATION", "CORTANA", "FACEBOOK", "IOS", "MSTEAMS", "OSS", "OSVC", "SERVICECLOUD", "SLACK", "TEST", "TWILIO", "WEB", "WEBHOOK"
        :type type: str

        :param session_expiry_duration_in_milliseconds:
            The value to assign to the session_expiry_duration_in_milliseconds property of this UpdateTwilioChannelDetails.
        :type session_expiry_duration_in_milliseconds: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTwilioChannelDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTwilioChannelDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param account_sid:
            The value to assign to the account_sid property of this UpdateTwilioChannelDetails.
        :type account_sid: str

        :param phone_number:
            The value to assign to the phone_number property of this UpdateTwilioChannelDetails.
        :type phone_number: str

        :param auth_token:
            The value to assign to the auth_token property of this UpdateTwilioChannelDetails.
        :type auth_token: str

        :param is_mms_enabled:
            The value to assign to the is_mms_enabled property of this UpdateTwilioChannelDetails.
        :type is_mms_enabled: bool

        :param original_connectors_url:
            The value to assign to the original_connectors_url property of this UpdateTwilioChannelDetails.
        :type original_connectors_url: str

        :param bot_id:
            The value to assign to the bot_id property of this UpdateTwilioChannelDetails.
        :type bot_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'type': 'str',
            'session_expiry_duration_in_milliseconds': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'account_sid': 'str',
            'phone_number': 'str',
            'auth_token': 'str',
            'is_mms_enabled': 'bool',
            'original_connectors_url': 'str',
            'bot_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'type': 'type',
            'session_expiry_duration_in_milliseconds': 'sessionExpiryDurationInMilliseconds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'account_sid': 'accountSID',
            'phone_number': 'phoneNumber',
            'auth_token': 'authToken',
            'is_mms_enabled': 'isMmsEnabled',
            'original_connectors_url': 'originalConnectorsUrl',
            'bot_id': 'botId'
        }

        self._description = None
        self._type = None
        self._session_expiry_duration_in_milliseconds = None
        self._freeform_tags = None
        self._defined_tags = None
        self._account_sid = None
        self._phone_number = None
        self._auth_token = None
        self._is_mms_enabled = None
        self._original_connectors_url = None
        self._bot_id = None
        self._type = 'TWILIO'

    @property
    def account_sid(self):
        """
        Gets the account_sid of this UpdateTwilioChannelDetails.
        The Account SID for the Twilio number.


        :return: The account_sid of this UpdateTwilioChannelDetails.
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """
        Sets the account_sid of this UpdateTwilioChannelDetails.
        The Account SID for the Twilio number.


        :param account_sid: The account_sid of this UpdateTwilioChannelDetails.
        :type: str
        """
        self._account_sid = account_sid

    @property
    def phone_number(self):
        """
        Gets the phone_number of this UpdateTwilioChannelDetails.
        The Twilio phone number.


        :return: The phone_number of this UpdateTwilioChannelDetails.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this UpdateTwilioChannelDetails.
        The Twilio phone number.


        :param phone_number: The phone_number of this UpdateTwilioChannelDetails.
        :type: str
        """
        self._phone_number = phone_number

    @property
    def auth_token(self):
        """
        Gets the auth_token of this UpdateTwilioChannelDetails.
        The Auth Token for the Twilio number.


        :return: The auth_token of this UpdateTwilioChannelDetails.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this UpdateTwilioChannelDetails.
        The Auth Token for the Twilio number.


        :param auth_token: The auth_token of this UpdateTwilioChannelDetails.
        :type: str
        """
        self._auth_token = auth_token

    @property
    def is_mms_enabled(self):
        """
        Gets the is_mms_enabled of this UpdateTwilioChannelDetails.
        Whether MMS is enabled for this channel or not.


        :return: The is_mms_enabled of this UpdateTwilioChannelDetails.
        :rtype: bool
        """
        return self._is_mms_enabled

    @is_mms_enabled.setter
    def is_mms_enabled(self, is_mms_enabled):
        """
        Sets the is_mms_enabled of this UpdateTwilioChannelDetails.
        Whether MMS is enabled for this channel or not.


        :param is_mms_enabled: The is_mms_enabled of this UpdateTwilioChannelDetails.
        :type: bool
        """
        self._is_mms_enabled = is_mms_enabled

    @property
    def original_connectors_url(self):
        """
        Gets the original_connectors_url of this UpdateTwilioChannelDetails.
        The original connectors URL (used for backward compatibility).


        :return: The original_connectors_url of this UpdateTwilioChannelDetails.
        :rtype: str
        """
        return self._original_connectors_url

    @original_connectors_url.setter
    def original_connectors_url(self, original_connectors_url):
        """
        Sets the original_connectors_url of this UpdateTwilioChannelDetails.
        The original connectors URL (used for backward compatibility).


        :param original_connectors_url: The original_connectors_url of this UpdateTwilioChannelDetails.
        :type: str
        """
        self._original_connectors_url = original_connectors_url

    @property
    def bot_id(self):
        """
        Gets the bot_id of this UpdateTwilioChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :return: The bot_id of this UpdateTwilioChannelDetails.
        :rtype: str
        """
        return self._bot_id

    @bot_id.setter
    def bot_id(self, bot_id):
        """
        Sets the bot_id of this UpdateTwilioChannelDetails.
        The ID of the Skill or Digital Assistant that the Channel is routed to.


        :param bot_id: The bot_id of this UpdateTwilioChannelDetails.
        :type: str
        """
        self._bot_id = bot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
