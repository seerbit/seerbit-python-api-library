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
from seerbit.client import Client
from seerbit.enums import EnvironmentEnum
from seerbit.exception import SeerbitError
from seerbit.httpclient import HttpClient
from seerbit.interface.service_interface import IService, IRequest
from seerbit.utility import Utility


class Service(IService, IRequest):
    _client: Client
    http_client: HttpClient
    message: str
    token: str
    response: dict

    def __init__(self, client: Client):
        """

        :param Client client:
            A non optional Client, the client with config

        """
        self._requires_token = False
        Utility.non_null(client)
        if not client.config.get("environment"):
            msg = "Client does not have correct environment. Use {0} or {1}"
            self.message = msg.format(EnvironmentEnum.LIVE.value, EnvironmentEnum.TEST.value)
            raise SeerbitError(self.message)
        if not client.config.get("public_key"):
            self.message = "Client doesn\'t have a merchant public key. Set a public key using the client"
            raise SeerbitError(self.message)
        if not client.config.get("private_key"):
            self.message = "Client doesn\'t have a merchant private key. Set a private key using the client"
            raise SeerbitError(self.message)
        self.http_client = HttpClient()
        Service._client = client

    @property
    def requires_token(self) -> bool:
        return self._requires_token

    @requires_token.setter
    def requires_token(self, is_required: bool):
        self._requires_token = is_required

    @property
    def client(self) -> Client:
        return Service._client

    @client.setter
    def client(self, client: Client):
        Utility.non_null(client)
        Service._client = client

    def post_request(self, endpoint, payload, token):
        message = "Set a field named \"api_base\" in the client configuration"
        Utility.require_non_null(self.client.config.get("api_base"), message)
        endpoint_url = str(self.client.config.get("api_base")) + endpoint
        json = self.http_client.post(self, endpoint_url, payload, token)
        return json.json()

    def put_request(self, endpoint, payload, token):
        message = "Set a field named \"api_base\" in the client configuration"
        Utility.require_non_null(self.client.config.get("api_base"), message)
        endpoint_url = str(self.client.config.get("api_base")) + endpoint
        json = self.http_client.put(self, endpoint_url, payload, token)
        return json.json()

    def get_request(self, endpoint, token):
        message = "Set a field named \"api_base\" in the client configuration"
        Utility.require_non_null(self.client.config.get("api_base"), message)
        endpoint_url = str(self.client.config.get("api_base")) + endpoint
        json = self.http_client.get(self, endpoint_url, token)
        return json.json()
