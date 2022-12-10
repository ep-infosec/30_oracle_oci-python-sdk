# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Subscription(object):
    """
    Subscription information for compartmentId. Only root compartments are allowed.
    """

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Subscription.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Subscription object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Subscription.
        :type id: str

        :param classic_subscription_id:
            The value to assign to the classic_subscription_id property of this Subscription.
        :type classic_subscription_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Subscription.
        :type compartment_id: str

        :param service_name:
            The value to assign to the service_name property of this Subscription.
        :type service_name: str

        :param is_classic_subscription:
            The value to assign to the is_classic_subscription property of this Subscription.
        :type is_classic_subscription: bool

        :param payment_model:
            The value to assign to the payment_model property of this Subscription.
        :type payment_model: str

        :param region_assignment:
            The value to assign to the region_assignment property of this Subscription.
        :type region_assignment: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Subscription.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param skus:
            The value to assign to the skus property of this Subscription.
        :type skus: list[oci.tenant_manager_control_plane.models.SubscriptionSku]

        :param program_type:
            The value to assign to the program_type property of this Subscription.
        :type program_type: str

        :param customer_country_code:
            The value to assign to the customer_country_code property of this Subscription.
        :type customer_country_code: str

        :param cloud_amount_currency:
            The value to assign to the cloud_amount_currency property of this Subscription.
        :type cloud_amount_currency: str

        :param csi_number:
            The value to assign to the csi_number property of this Subscription.
        :type csi_number: str

        :param subscription_tier:
            The value to assign to the subscription_tier property of this Subscription.
        :type subscription_tier: str

        :param is_government_subscription:
            The value to assign to the is_government_subscription property of this Subscription.
        :type is_government_subscription: bool

        :param promotion:
            The value to assign to the promotion property of this Subscription.
        :type promotion: list[oci.tenant_manager_control_plane.models.Promotion]

        :param purchase_entitlement_id:
            The value to assign to the purchase_entitlement_id property of this Subscription.
        :type purchase_entitlement_id: str

        :param start_date:
            The value to assign to the start_date property of this Subscription.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this Subscription.
        :type end_date: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Subscription.
        :type time_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this Subscription.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'classic_subscription_id': 'str',
            'compartment_id': 'str',
            'service_name': 'str',
            'is_classic_subscription': 'bool',
            'payment_model': 'str',
            'region_assignment': 'str',
            'lifecycle_state': 'str',
            'skus': 'list[SubscriptionSku]',
            'program_type': 'str',
            'customer_country_code': 'str',
            'cloud_amount_currency': 'str',
            'csi_number': 'str',
            'subscription_tier': 'str',
            'is_government_subscription': 'bool',
            'promotion': 'list[Promotion]',
            'purchase_entitlement_id': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'time_updated': 'datetime',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'classic_subscription_id': 'classicSubscriptionId',
            'compartment_id': 'compartmentId',
            'service_name': 'serviceName',
            'is_classic_subscription': 'isClassicSubscription',
            'payment_model': 'paymentModel',
            'region_assignment': 'regionAssignment',
            'lifecycle_state': 'lifecycleState',
            'skus': 'skus',
            'program_type': 'programType',
            'customer_country_code': 'customerCountryCode',
            'cloud_amount_currency': 'cloudAmountCurrency',
            'csi_number': 'csiNumber',
            'subscription_tier': 'subscriptionTier',
            'is_government_subscription': 'isGovernmentSubscription',
            'promotion': 'promotion',
            'purchase_entitlement_id': 'purchaseEntitlementId',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'time_updated': 'timeUpdated',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._classic_subscription_id = None
        self._compartment_id = None
        self._service_name = None
        self._is_classic_subscription = None
        self._payment_model = None
        self._region_assignment = None
        self._lifecycle_state = None
        self._skus = None
        self._program_type = None
        self._customer_country_code = None
        self._cloud_amount_currency = None
        self._csi_number = None
        self._subscription_tier = None
        self._is_government_subscription = None
        self._promotion = None
        self._purchase_entitlement_id = None
        self._start_date = None
        self._end_date = None
        self._time_updated = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Subscription.
        OCID of the subscription details for the particular root compartment or tenancy.


        :return: The id of this Subscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscription.
        OCID of the subscription details for the particular root compartment or tenancy.


        :param id: The id of this Subscription.
        :type: str
        """
        self._id = id

    @property
    def classic_subscription_id(self):
        """
        **[Required]** Gets the classic_subscription_id of this Subscription.
        Classic subscription ID.


        :return: The classic_subscription_id of this Subscription.
        :rtype: str
        """
        return self._classic_subscription_id

    @classic_subscription_id.setter
    def classic_subscription_id(self, classic_subscription_id):
        """
        Sets the classic_subscription_id of this Subscription.
        Classic subscription ID.


        :param classic_subscription_id: The classic_subscription_id of this Subscription.
        :type: str
        """
        self._classic_subscription_id = classic_subscription_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Subscription.
        OCID of the compartment. Always a tenancy OCID.


        :return: The compartment_id of this Subscription.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Subscription.
        OCID of the compartment. Always a tenancy OCID.


        :param compartment_id: The compartment_id of this Subscription.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this Subscription.
        The type of subscription, such as 'CLOUDCM', 'SAAS', 'ERP', or 'CRM'.


        :return: The service_name of this Subscription.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this Subscription.
        The type of subscription, such as 'CLOUDCM', 'SAAS', 'ERP', or 'CRM'.


        :param service_name: The service_name of this Subscription.
        :type: str
        """
        self._service_name = service_name

    @property
    def is_classic_subscription(self):
        """
        Gets the is_classic_subscription of this Subscription.
        Denotes if the subscription is from classic systems or not.


        :return: The is_classic_subscription of this Subscription.
        :rtype: bool
        """
        return self._is_classic_subscription

    @is_classic_subscription.setter
    def is_classic_subscription(self, is_classic_subscription):
        """
        Sets the is_classic_subscription of this Subscription.
        Denotes if the subscription is from classic systems or not.


        :param is_classic_subscription: The is_classic_subscription of this Subscription.
        :type: bool
        """
        self._is_classic_subscription = is_classic_subscription

    @property
    def payment_model(self):
        """
        Gets the payment_model of this Subscription.
        The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.


        :return: The payment_model of this Subscription.
        :rtype: str
        """
        return self._payment_model

    @payment_model.setter
    def payment_model(self, payment_model):
        """
        Sets the payment_model of this Subscription.
        The pay model of the subscription, such as 'Pay as you go' or 'Monthly'.


        :param payment_model: The payment_model of this Subscription.
        :type: str
        """
        self._payment_model = payment_model

    @property
    def region_assignment(self):
        """
        Gets the region_assignment of this Subscription.
        Region for the subscription.


        :return: The region_assignment of this Subscription.
        :rtype: str
        """
        return self._region_assignment

    @region_assignment.setter
    def region_assignment(self, region_assignment):
        """
        Sets the region_assignment of this Subscription.
        Region for the subscription.


        :param region_assignment: The region_assignment of this Subscription.
        :type: str
        """
        self._region_assignment = region_assignment

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Subscription.
        Lifecycle state of the subscription.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Subscription.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Subscription.
        Lifecycle state of the subscription.


        :param lifecycle_state: The lifecycle_state of this Subscription.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def skus(self):
        """
        Gets the skus of this Subscription.
        List of SKUs linked to this subscription.


        :return: The skus of this Subscription.
        :rtype: list[oci.tenant_manager_control_plane.models.SubscriptionSku]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """
        Sets the skus of this Subscription.
        List of SKUs linked to this subscription.


        :param skus: The skus of this Subscription.
        :type: list[oci.tenant_manager_control_plane.models.SubscriptionSku]
        """
        self._skus = skus

    @property
    def program_type(self):
        """
        Gets the program_type of this Subscription.
        Denotes any program that is associated with the subscription.


        :return: The program_type of this Subscription.
        :rtype: str
        """
        return self._program_type

    @program_type.setter
    def program_type(self, program_type):
        """
        Sets the program_type of this Subscription.
        Denotes any program that is associated with the subscription.


        :param program_type: The program_type of this Subscription.
        :type: str
        """
        self._program_type = program_type

    @property
    def customer_country_code(self):
        """
        Gets the customer_country_code of this Subscription.
        The country code for the customer associated with the subscription.


        :return: The customer_country_code of this Subscription.
        :rtype: str
        """
        return self._customer_country_code

    @customer_country_code.setter
    def customer_country_code(self, customer_country_code):
        """
        Sets the customer_country_code of this Subscription.
        The country code for the customer associated with the subscription.


        :param customer_country_code: The customer_country_code of this Subscription.
        :type: str
        """
        self._customer_country_code = customer_country_code

    @property
    def cloud_amount_currency(self):
        """
        Gets the cloud_amount_currency of this Subscription.
        The currency code for the customer associated with the subscription.


        :return: The cloud_amount_currency of this Subscription.
        :rtype: str
        """
        return self._cloud_amount_currency

    @cloud_amount_currency.setter
    def cloud_amount_currency(self, cloud_amount_currency):
        """
        Sets the cloud_amount_currency of this Subscription.
        The currency code for the customer associated with the subscription.


        :param cloud_amount_currency: The cloud_amount_currency of this Subscription.
        :type: str
        """
        self._cloud_amount_currency = cloud_amount_currency

    @property
    def csi_number(self):
        """
        Gets the csi_number of this Subscription.
        Customer service identifier for the customer associated with the subscription.


        :return: The csi_number of this Subscription.
        :rtype: str
        """
        return self._csi_number

    @csi_number.setter
    def csi_number(self, csi_number):
        """
        Sets the csi_number of this Subscription.
        Customer service identifier for the customer associated with the subscription.


        :param csi_number: The csi_number of this Subscription.
        :type: str
        """
        self._csi_number = csi_number

    @property
    def subscription_tier(self):
        """
        Gets the subscription_tier of this Subscription.
        Tier for the subscription, such as if it is a free promotion subscription or a paid subscription.


        :return: The subscription_tier of this Subscription.
        :rtype: str
        """
        return self._subscription_tier

    @subscription_tier.setter
    def subscription_tier(self, subscription_tier):
        """
        Sets the subscription_tier of this Subscription.
        Tier for the subscription, such as if it is a free promotion subscription or a paid subscription.


        :param subscription_tier: The subscription_tier of this Subscription.
        :type: str
        """
        self._subscription_tier = subscription_tier

    @property
    def is_government_subscription(self):
        """
        Gets the is_government_subscription of this Subscription.
        Denotes if the subscription is a government subscription or not.


        :return: The is_government_subscription of this Subscription.
        :rtype: bool
        """
        return self._is_government_subscription

    @is_government_subscription.setter
    def is_government_subscription(self, is_government_subscription):
        """
        Sets the is_government_subscription of this Subscription.
        Denotes if the subscription is a government subscription or not.


        :param is_government_subscription: The is_government_subscription of this Subscription.
        :type: bool
        """
        self._is_government_subscription = is_government_subscription

    @property
    def promotion(self):
        """
        Gets the promotion of this Subscription.
        List of promotions related to the subscription.


        :return: The promotion of this Subscription.
        :rtype: list[oci.tenant_manager_control_plane.models.Promotion]
        """
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """
        Sets the promotion of this Subscription.
        List of promotions related to the subscription.


        :param promotion: The promotion of this Subscription.
        :type: list[oci.tenant_manager_control_plane.models.Promotion]
        """
        self._promotion = promotion

    @property
    def purchase_entitlement_id(self):
        """
        Gets the purchase_entitlement_id of this Subscription.
        Purchase entitlement id associated with the subscription.


        :return: The purchase_entitlement_id of this Subscription.
        :rtype: str
        """
        return self._purchase_entitlement_id

    @purchase_entitlement_id.setter
    def purchase_entitlement_id(self, purchase_entitlement_id):
        """
        Sets the purchase_entitlement_id of this Subscription.
        Purchase entitlement id associated with the subscription.


        :param purchase_entitlement_id: The purchase_entitlement_id of this Subscription.
        :type: str
        """
        self._purchase_entitlement_id = purchase_entitlement_id

    @property
    def start_date(self):
        """
        Gets the start_date of this Subscription.
        Subscription start time.


        :return: The start_date of this Subscription.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Subscription.
        Subscription start time.


        :param start_date: The start_date of this Subscription.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this Subscription.
        Subscription end time.


        :return: The end_date of this Subscription.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this Subscription.
        Subscription end time.


        :param end_date: The end_date of this Subscription.
        :type: datetime
        """
        self._end_date = end_date

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Subscription.
        Date-time when subscription is updated.


        :return: The time_updated of this Subscription.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Subscription.
        Date-time when subscription is updated.


        :param time_updated: The time_updated of this Subscription.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_created(self):
        """
        Gets the time_created of this Subscription.
        Date-time when subscription is created.


        :return: The time_created of this Subscription.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Subscription.
        Date-time when subscription is created.


        :param time_created: The time_created of this Subscription.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
