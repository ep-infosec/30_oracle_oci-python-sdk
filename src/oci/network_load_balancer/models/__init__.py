# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .backend import Backend
from .backend_collection import BackendCollection
from .backend_details import BackendDetails
from .backend_health import BackendHealth
from .backend_set import BackendSet
from .backend_set_collection import BackendSetCollection
from .backend_set_details import BackendSetDetails
from .backend_set_health import BackendSetHealth
from .backend_set_summary import BackendSetSummary
from .backend_summary import BackendSummary
from .change_network_load_balancer_compartment_details import ChangeNetworkLoadBalancerCompartmentDetails
from .create_backend_details import CreateBackendDetails
from .create_backend_set_details import CreateBackendSetDetails
from .create_listener_details import CreateListenerDetails
from .create_network_load_balancer_details import CreateNetworkLoadBalancerDetails
from .health_check_result import HealthCheckResult
from .health_checker import HealthChecker
from .health_checker_details import HealthCheckerDetails
from .ip_address import IpAddress
from .listener import Listener
from .listener_collection import ListenerCollection
from .listener_details import ListenerDetails
from .listener_summary import ListenerSummary
from .network_load_balancer import NetworkLoadBalancer
from .network_load_balancer_collection import NetworkLoadBalancerCollection
from .network_load_balancer_health import NetworkLoadBalancerHealth
from .network_load_balancer_health_collection import NetworkLoadBalancerHealthCollection
from .network_load_balancer_health_summary import NetworkLoadBalancerHealthSummary
from .network_load_balancer_summary import NetworkLoadBalancerSummary
from .network_load_balancers_policy_collection import NetworkLoadBalancersPolicyCollection
from .network_load_balancers_protocol_collection import NetworkLoadBalancersProtocolCollection
from .reserved_ip import ReservedIP
from .update_backend_details import UpdateBackendDetails
from .update_backend_set_details import UpdateBackendSetDetails
from .update_health_checker_details import UpdateHealthCheckerDetails
from .update_listener_details import UpdateListenerDetails
from .update_network_load_balancer_details import UpdateNetworkLoadBalancerDetails
from .update_network_security_groups_details import UpdateNetworkSecurityGroupsDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for network_load_balancer services.
network_load_balancer_type_mapping = {
    "Backend": Backend,
    "BackendCollection": BackendCollection,
    "BackendDetails": BackendDetails,
    "BackendHealth": BackendHealth,
    "BackendSet": BackendSet,
    "BackendSetCollection": BackendSetCollection,
    "BackendSetDetails": BackendSetDetails,
    "BackendSetHealth": BackendSetHealth,
    "BackendSetSummary": BackendSetSummary,
    "BackendSummary": BackendSummary,
    "ChangeNetworkLoadBalancerCompartmentDetails": ChangeNetworkLoadBalancerCompartmentDetails,
    "CreateBackendDetails": CreateBackendDetails,
    "CreateBackendSetDetails": CreateBackendSetDetails,
    "CreateListenerDetails": CreateListenerDetails,
    "CreateNetworkLoadBalancerDetails": CreateNetworkLoadBalancerDetails,
    "HealthCheckResult": HealthCheckResult,
    "HealthChecker": HealthChecker,
    "HealthCheckerDetails": HealthCheckerDetails,
    "IpAddress": IpAddress,
    "Listener": Listener,
    "ListenerCollection": ListenerCollection,
    "ListenerDetails": ListenerDetails,
    "ListenerSummary": ListenerSummary,
    "NetworkLoadBalancer": NetworkLoadBalancer,
    "NetworkLoadBalancerCollection": NetworkLoadBalancerCollection,
    "NetworkLoadBalancerHealth": NetworkLoadBalancerHealth,
    "NetworkLoadBalancerHealthCollection": NetworkLoadBalancerHealthCollection,
    "NetworkLoadBalancerHealthSummary": NetworkLoadBalancerHealthSummary,
    "NetworkLoadBalancerSummary": NetworkLoadBalancerSummary,
    "NetworkLoadBalancersPolicyCollection": NetworkLoadBalancersPolicyCollection,
    "NetworkLoadBalancersProtocolCollection": NetworkLoadBalancersProtocolCollection,
    "ReservedIP": ReservedIP,
    "UpdateBackendDetails": UpdateBackendDetails,
    "UpdateBackendSetDetails": UpdateBackendSetDetails,
    "UpdateHealthCheckerDetails": UpdateHealthCheckerDetails,
    "UpdateListenerDetails": UpdateListenerDetails,
    "UpdateNetworkLoadBalancerDetails": UpdateNetworkLoadBalancerDetails,
    "UpdateNetworkSecurityGroupsDetails": UpdateNetworkSecurityGroupsDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
