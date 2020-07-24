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
import json

from seerbit.interface.app_interface import IClientConstants, INumericConstants
from seerbit.client import Client
from seerbit.config import Config
from seerbit.interface.service_interface import IAuthentication
from seerbit.service.servicelib import Service
from seerbit.utility import Utility


class Authentication(IAuthentication, Service, IClientConstants, INumericConstants):

    def __init__(self, client: Client):
        super(Authentication, self).__init__(client)
        Utility.non_null(client)

    def auth(self):
        """ POST /api/v2/encrypt/keys """
        config: Config = self.client.config
        payload: dict = {
            "key": None
        }
        key = config.private_key + "." + config.public_key
        payload["key"] = key
        print("request: " + json.dumps(payload))
        self.response = self.post_request(IClientConstants.AUTHENTICATION_ENDPOINT, payload, None)
        return self.response

    def get_token(self) -> str:
        encrypted_key: str = ""
        if self.response:
            if "data" in self.response:
                encrypted_key_dict = self.response["data"]
                if "EncryptedSecKey" in encrypted_key_dict:
                    encrypted_key_dict = encrypted_key_dict["EncryptedSecKey"]
                    encrypted_key = encrypted_key_dict.get("encryptedKey")
        return encrypted_key