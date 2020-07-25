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
from seerbit.service.recurring_service import RecurringService

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


def update_subscription(token_str: str):
    """ Initiate Recurrent Subscription """
    print("================== start update subscription ==================")
    recurring_payload = {
        "amount": "200",
        "currency": "NGN",
        "country": "NG",
        "mobileNumber": "08033456500",
        "billingId": "PUBK_PjQ5d1578650322483",
        "publicKey": client.public_key,
        "status": "INACTIVE"
    }
    recurring_service = RecurringService(client, token_str)
    json_response = recurring_service.update_subscription(recurring_payload)
    print("================== stop update subscription ==================")
    return json_response


token = authenticate()

if token:
    print("update subscription response: " + str(update_subscription(token)))
else:
    print("authentication failure")
