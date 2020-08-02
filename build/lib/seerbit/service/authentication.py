"""
  Copyright (C) 2020 Seerbit

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
from base64 import b64encode
from seerbit.exception import SeerbitError
from seerbit.interface.app_interface import IClientConstants, INumericConstants
from seerbit.client import Client
from seerbit.config import Config
from seerbit.interface.service_interface import IAuthentication
from seerbit.service.servicelib import Service
from seerbit.utility import Utility


class Authentication(IAuthentication, Service, IClientConstants, INumericConstants):

    def __init__(self, client: Client):
        """

        :param Client client:
            A non optional Client, the client with config

        """
        super(Authentication, self).__init__(client)
        Utility.non_null(client)

    def auth(self):
        """

        POST /api/v2/encrypt/keys

        :returns Any self.response

        """
        config: Config = self.client.config
        payload: dict = {
            "key": None
        }
        key = config.private_key + "." + config.public_key
        payload["key"] = key
        self.response = self.post_request(IClientConstants.AUTHENTICATION_ENDPOINT, payload, None)
        return self.response

    def get_token(self) -> str:
        """

        :return str encrypted_key

        """
        encrypted_key: str = ""
        if self.response:
            if "data" in self.response:
                encrypted_key_dict = self.response["data"]
                if "EncryptedSecKey" in encrypted_key_dict:
                    encrypted_key_dict = encrypted_key_dict["EncryptedSecKey"]
                    encrypted_key = encrypted_key_dict.get("encryptedKey")
        return encrypted_key

    def get_basic_auth_encoded_string(self) -> str:
        """

        :return str base 64 encoded string

        """
        client = self.client
        authentication_scheme = client.authentication_scheme
        if authentication_scheme.lower() not in ["basic ", "bearer "]:
            raise SeerbitError("Set authentication scheme to AuthTypeEnum.BASIC value before calling this method")
        authorization_str = client.public_key + ":" + client.private_key
        encoded_bytes = b64encode(authorization_str.encode("utf-8"))
        encoded_str = str(encoded_bytes, "utf-8")
        return encoded_str
