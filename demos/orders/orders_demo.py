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
from seerbit.service.order_service import OrderService

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


def order(token_str: str):
    """ Initiate Order """
    print("================== start order ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    order_payload = {
        "email": "johndoe@gmail.com",
        "publicKey": client.public_key,
        "paymentReference": payment_ref,
        "fullName": "John Doe",
        "orderType": "BULK_BULK",
        "mobileNumber": "08000000001",
        "callbackUrl": "https://yourdomain.com",
        "country": "NG",
        "currency": "NGN",
        "amount": "1400",
        "orders": [
            {
                "orderId": "22S789420214623",
                "currency": "NGN",
                "amount": "500.00",
                "productId": "fruits",
                "productDescription": "mango"
            },
            {
                "orderId": "1a3sa82748272556947",
                "currency": "NGN",
                "amount": "900.00",
                "productId": "fruits",
                "productDescription": "orange"
            }
        ]
    }
    order_service = OrderService(client, token_str)
    json_response = order_service.authorize(order_payload)
    print("================== stop order ==================")
    return json_response


token = authenticate()

if token:
    print("order response: " + str(order(token)))
else:
    print("authentication failure")
