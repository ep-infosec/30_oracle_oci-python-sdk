# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomEndpointDetails(object):
    """
    Details for a custom endpoint for the vb instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this CustomEndpointDetails.
        :type hostname: str

        :param certificate_secret_id:
            The value to assign to the certificate_secret_id property of this CustomEndpointDetails.
        :type certificate_secret_id: str

        :param certificate_secret_version:
            The value to assign to the certificate_secret_version property of this CustomEndpointDetails.
        :type certificate_secret_version: int

        """
        self.swagger_types = {
            'hostname': 'str',
            'certificate_secret_id': 'str',
            'certificate_secret_version': 'int'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'certificate_secret_id': 'certificateSecretId',
            'certificate_secret_version': 'certificateSecretVersion'
        }

        self._hostname = None
        self._certificate_secret_id = None
        self._certificate_secret_version = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this CustomEndpointDetails.
        A custom hostname to be used for the vb instance URL, in FQDN format.


        :return: The hostname of this CustomEndpointDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CustomEndpointDetails.
        A custom hostname to be used for the vb instance URL, in FQDN format.


        :param hostname: The hostname of this CustomEndpointDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def certificate_secret_id(self):
        """
        Gets the certificate_secret_id of this CustomEndpointDetails.
        Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.


        :return: The certificate_secret_id of this CustomEndpointDetails.
        :rtype: str
        """
        return self._certificate_secret_id

    @certificate_secret_id.setter
    def certificate_secret_id(self, certificate_secret_id):
        """
        Sets the certificate_secret_id of this CustomEndpointDetails.
        Optional OCID of a vault/secret containing a private SSL certificate bundle to be used for the custom hostname.


        :param certificate_secret_id: The certificate_secret_id of this CustomEndpointDetails.
        :type: str
        """
        self._certificate_secret_id = certificate_secret_id

    @property
    def certificate_secret_version(self):
        """
        Gets the certificate_secret_version of this CustomEndpointDetails.
        The secret version used for the certificate-secret-id (if certificate-secret-id is specified).


        :return: The certificate_secret_version of this CustomEndpointDetails.
        :rtype: int
        """
        return self._certificate_secret_version

    @certificate_secret_version.setter
    def certificate_secret_version(self, certificate_secret_version):
        """
        Sets the certificate_secret_version of this CustomEndpointDetails.
        The secret version used for the certificate-secret-id (if certificate-secret-id is specified).


        :param certificate_secret_version: The certificate_secret_version of this CustomEndpointDetails.
        :type: int
        """
        self._certificate_secret_version = certificate_secret_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
