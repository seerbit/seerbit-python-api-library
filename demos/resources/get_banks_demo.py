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
from seerbit.config import Config
from seerbit.enums import EnvironmentEnum
from seerbit.seerbitlib import Seerbit
from seerbit.service.authentication import Authentication
from seerbit.service.resource_service import ResourceService

client = Client()


def authenticate() -> str:
    """ User authentication token """
    print("================== start authentication ==================")
    client.api_base = Seerbit.LIVE_API_BASE
    client.environment = EnvironmentEnum.LIVE.value
    config = Config()
    config.put("public_key", "public2key")
    config.put("private_key", "private2key")
    client.config = config
    client.timeout = 20
    auth_service = Authentication(client)
    auth_service.auth()
    print("================== stop authentication ==================")
    return auth_service.get_token()


def get_bank_list(token_str: str):
    """ Get Transaction Status """
    print("================== start get bank list ==================")
    resource_service = ResourceService(client, token_str)
    json_response = resource_service.get_bank_list(client.public_key)
    print("================== stop get bank list ==================")
    return json_response


token = authenticate()

if token:
    billing_id = "367567478"
    print("get bank list response: " + str(get_bank_list(token)))
else:
    print("authentication failure")
