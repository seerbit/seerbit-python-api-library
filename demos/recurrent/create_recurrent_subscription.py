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


def subscribe(token_str: str):
    """ Initiate Recurrent Subscription """
    print("================== start subscription ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    recurring_payload = {
        "publicKey": client.public_key,
        "paymentReference": payment_ref,
        "planId": "",
        "cardNumber": "2223000000000007",
        "expiryMonth": "05",
        "callbackUrl": "https://checkout.seerbitapi.com",
        "expiryYear": "21",
        "cvv": "100",
        "amount": "20",
        "currency": "NGN",
        "productDescription": "Test Token",
        "productId": "Terrain",
        "country": "NG",
        "startDate": "2019-01-11",
        "cardName": "Bola Olat",
        "billingCycle": "DAILY",
        "email": "johndoe@gmail.com",
        "mobileNumber": "09022323537",
        "billingPeriod": "4",
        "subscriptionAmount": False
    }
    recurring_service = RecurringService(client, token_str)
    json_response = recurring_service.create_subscription(recurring_payload)
    print("================== stop subscription ==================")
    return json_response


token = authenticate()

if token:
    print("subscription response: " + str(subscribe(token)))
else:
    print("authentication failure")
