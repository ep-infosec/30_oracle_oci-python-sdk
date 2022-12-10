# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .payment_option import PaymentOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreditCardPaymentOption(PaymentOption):
    """
    Credit card Payment related details
    """

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "VISA"
    CREDIT_CARD_TYPE_VISA = "VISA"

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "AMEX"
    CREDIT_CARD_TYPE_AMEX = "AMEX"

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "MASTERCARD"
    CREDIT_CARD_TYPE_MASTERCARD = "MASTERCARD"

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "DISCOVER"
    CREDIT_CARD_TYPE_DISCOVER = "DISCOVER"

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "JCB"
    CREDIT_CARD_TYPE_JCB = "JCB"

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "DINER"
    CREDIT_CARD_TYPE_DINER = "DINER"

    #: A constant which can be used with the credit_card_type property of a CreditCardPaymentOption.
    #: This constant has a value of "ELO"
    CREDIT_CARD_TYPE_ELO = "ELO"

    def __init__(self, **kwargs):
        """
        Initializes a new CreditCardPaymentOption object with values from keyword arguments. The default value of the :py:attr:`~oci.osp_gateway.models.CreditCardPaymentOption.payment_method` attribute
        of this class is ``CREDIT_CARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param wallet_instrument_id:
            The value to assign to the wallet_instrument_id property of this CreditCardPaymentOption.
        :type wallet_instrument_id: str

        :param wallet_transaction_id:
            The value to assign to the wallet_transaction_id property of this CreditCardPaymentOption.
        :type wallet_transaction_id: str

        :param payment_method:
            The value to assign to the payment_method property of this CreditCardPaymentOption.
            Allowed values for this property are: "CREDIT_CARD", "PAYPAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type payment_method: str

        :param credit_card_type:
            The value to assign to the credit_card_type property of this CreditCardPaymentOption.
            Allowed values for this property are: "VISA", "AMEX", "MASTERCARD", "DISCOVER", "JCB", "DINER", "ELO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credit_card_type: str

        :param last_digits:
            The value to assign to the last_digits property of this CreditCardPaymentOption.
        :type last_digits: str

        :param name_on_card:
            The value to assign to the name_on_card property of this CreditCardPaymentOption.
        :type name_on_card: str

        :param time_expiration:
            The value to assign to the time_expiration property of this CreditCardPaymentOption.
        :type time_expiration: datetime

        """
        self.swagger_types = {
            'wallet_instrument_id': 'str',
            'wallet_transaction_id': 'str',
            'payment_method': 'str',
            'credit_card_type': 'str',
            'last_digits': 'str',
            'name_on_card': 'str',
            'time_expiration': 'datetime'
        }

        self.attribute_map = {
            'wallet_instrument_id': 'walletInstrumentId',
            'wallet_transaction_id': 'walletTransactionId',
            'payment_method': 'paymentMethod',
            'credit_card_type': 'creditCardType',
            'last_digits': 'lastDigits',
            'name_on_card': 'nameOnCard',
            'time_expiration': 'timeExpiration'
        }

        self._wallet_instrument_id = None
        self._wallet_transaction_id = None
        self._payment_method = None
        self._credit_card_type = None
        self._last_digits = None
        self._name_on_card = None
        self._time_expiration = None
        self._payment_method = 'CREDIT_CARD'

    @property
    def credit_card_type(self):
        """
        Gets the credit_card_type of this CreditCardPaymentOption.
        Credit card type.

        Allowed values for this property are: "VISA", "AMEX", "MASTERCARD", "DISCOVER", "JCB", "DINER", "ELO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credit_card_type of this CreditCardPaymentOption.
        :rtype: str
        """
        return self._credit_card_type

    @credit_card_type.setter
    def credit_card_type(self, credit_card_type):
        """
        Sets the credit_card_type of this CreditCardPaymentOption.
        Credit card type.


        :param credit_card_type: The credit_card_type of this CreditCardPaymentOption.
        :type: str
        """
        allowed_values = ["VISA", "AMEX", "MASTERCARD", "DISCOVER", "JCB", "DINER", "ELO"]
        if not value_allowed_none_or_none_sentinel(credit_card_type, allowed_values):
            credit_card_type = 'UNKNOWN_ENUM_VALUE'
        self._credit_card_type = credit_card_type

    @property
    def last_digits(self):
        """
        Gets the last_digits of this CreditCardPaymentOption.
        Last four digits of the card.


        :return: The last_digits of this CreditCardPaymentOption.
        :rtype: str
        """
        return self._last_digits

    @last_digits.setter
    def last_digits(self, last_digits):
        """
        Sets the last_digits of this CreditCardPaymentOption.
        Last four digits of the card.


        :param last_digits: The last_digits of this CreditCardPaymentOption.
        :type: str
        """
        self._last_digits = last_digits

    @property
    def name_on_card(self):
        """
        Gets the name_on_card of this CreditCardPaymentOption.
        Name on the credit card.


        :return: The name_on_card of this CreditCardPaymentOption.
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """
        Sets the name_on_card of this CreditCardPaymentOption.
        Name on the credit card.


        :param name_on_card: The name_on_card of this CreditCardPaymentOption.
        :type: str
        """
        self._name_on_card = name_on_card

    @property
    def time_expiration(self):
        """
        Gets the time_expiration of this CreditCardPaymentOption.
        Expired date of the credit card.


        :return: The time_expiration of this CreditCardPaymentOption.
        :rtype: datetime
        """
        return self._time_expiration

    @time_expiration.setter
    def time_expiration(self, time_expiration):
        """
        Sets the time_expiration of this CreditCardPaymentOption.
        Expired date of the credit card.


        :param time_expiration: The time_expiration of this CreditCardPaymentOption.
        :type: datetime
        """
        self._time_expiration = time_expiration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other