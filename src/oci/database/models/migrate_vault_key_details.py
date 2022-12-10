# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrateVaultKeyDetails(object):
    """
    Details for replacing existing Oracle-managed keys with customer-managed `Vault service`__ keys and vice-versa is not supported.

    __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrateVaultKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this MigrateVaultKeyDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this MigrateVaultKeyDetails.
        :type kms_key_version_id: str

        :param vault_id:
            The value to assign to the vault_id property of this MigrateVaultKeyDetails.
        :type vault_id: str

        :param tde_wallet_password:
            The value to assign to the tde_wallet_password property of this MigrateVaultKeyDetails.
        :type tde_wallet_password: str

        :param admin_password:
            The value to assign to the admin_password property of this MigrateVaultKeyDetails.
        :type admin_password: str

        """
        self.swagger_types = {
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'vault_id': 'str',
            'tde_wallet_password': 'str',
            'admin_password': 'str'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'vault_id': 'vaultId',
            'tde_wallet_password': 'tdeWalletPassword',
            'admin_password': 'adminPassword'
        }

        self._kms_key_id = None
        self._kms_key_version_id = None
        self._vault_id = None
        self._tde_wallet_password = None
        self._admin_password = None

    @property
    def kms_key_id(self):
        """
        **[Required]** Gets the kms_key_id of this MigrateVaultKeyDetails.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this MigrateVaultKeyDetails.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this MigrateVaultKeyDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_version_id(self):
        """
        Gets the kms_key_version_id of this MigrateVaultKeyDetails.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :return: The kms_key_version_id of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this MigrateVaultKeyDetails.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :param kms_key_version_id: The kms_key_version_id of this MigrateVaultKeyDetails.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this MigrateVaultKeyDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this MigrateVaultKeyDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this MigrateVaultKeyDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def tde_wallet_password(self):
        """
        Gets the tde_wallet_password of this MigrateVaultKeyDetails.
        The existing TDE wallet password of the database.


        :return: The tde_wallet_password of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._tde_wallet_password

    @tde_wallet_password.setter
    def tde_wallet_password(self, tde_wallet_password):
        """
        Sets the tde_wallet_password of this MigrateVaultKeyDetails.
        The existing TDE wallet password of the database.


        :param tde_wallet_password: The tde_wallet_password of this MigrateVaultKeyDetails.
        :type: str
        """
        self._tde_wallet_password = tde_wallet_password

    @property
    def admin_password(self):
        """
        Gets the admin_password of this MigrateVaultKeyDetails.
        The existing admin password of the database.


        :return: The admin_password of this MigrateVaultKeyDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this MigrateVaultKeyDetails.
        The existing admin password of the database.


        :param admin_password: The admin_password of this MigrateVaultKeyDetails.
        :type: str
        """
        self._admin_password = admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
