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
from seerbit.service.mobile_money_service import MobileMoneyService

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


def mobile_money(token_str: str):
    """ Initiate Mobile Money Payment """
    print("================== start mobile money ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    mobile_money_payload = {
        "fullName": "john doe",
        "email": "johndoe@gmail.com",
        "mobileNumber": "08022343345",
        "publicKey": client.public_key,
        "paymentReference": payment_ref,
        "deviceType": "nokia 3310",
        "sourceIP": "1.0.1.0",
        "currency": "UGX",
        "productDescription": "snacks",
        "country": "UG",
        "fee": "1.00",
        "network": "MTN",
        "voucherCode": "",
        "amount": "10.01",
        "productId": "grocery",
        "paymentType": "MOMO"
    }
    mobile_money_service = MobileMoneyService(client, token_str)
    json_response = mobile_money_service.authorize(mobile_money_payload)
    print("================== stop mobile money ==================")
    return json_response


token = authenticate()

if token:
    print("mobile money response: " + str(mobile_money(token)))
else:
    print("authentication failure")
