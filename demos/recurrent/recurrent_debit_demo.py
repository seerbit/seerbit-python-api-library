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
from random import randint
from seerbit.client import Client
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
    client.private_key = "public2key"
    client.public_key = "private2key"
    client.timeout = 20
    auth_service = Authentication(client)
    auth_service.auth()
    print("================== stop authentication ==================")
    return auth_service.get_token()


def recurring_debit(token_str: str):
    """ Initiate Recurring Debit """
    print("================== start recurring debit ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    recurring_payload = {
        "amount": "200",
        "publicKey": client.public_key,
        "email": "john.doe@centricgateway.com",
        "authorizationCode": "1234567898765325",
        "paymentReference": payment_ref,
        "currency": "NGN"
    }
    recurring_service = RecurringService(client, token_str)
    json_response = recurring_service.recurring_debit(recurring_payload)
    print("================== stop recurring debit ==================")
    return json_response


token = authenticate()

if token:
    print("recurring debit response: " + str(recurring_debit(token)))
else:
    print("authentication failure")
