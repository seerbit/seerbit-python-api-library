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
from seerbit.seerbitlib import Seerbit
from seerbit.service.authentication import Authentication
from seerbit.service.resource_service import ResourceService
from seerbit.service.standard_checkout_service import StandardCheckoutService

client = Client()


def authenticate() -> str:
    """ User authentication token """
    print("================== start authentication ==================")
    client.api_base = Seerbit.LIVE_API_BASE
    client.environment = EnvironmentEnum.LIVE.value
    client.private_key = "private_key"
    client.public_key = "public_key"
    client.timeout = 20
    auth_service = Authentication(client)
    auth_service.auth()
    print("================== stop authentication ==================")
    return auth_service.get_token()


def initialize_transaction(token_str: str):
    """ Initialize Transaction """
    print("================== start initialize transaction ==================")
    standard_checkout_service = StandardCheckoutService(client, token_str)
    hash_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "currency": "KES",
        "country": "KE",
        "paymentReference": "643108207791261657324A3",
        "email": "test@yourdomain.com",
        "productId": "productID",
        "productDescription": "WEIGHING AND ADMIN CHARGES",
        "callbackUrl": "http://yourdomain.com"
    }
    hash_str = standard_checkout_service.get_hash(hash_payload)
    standard_checkout_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "currency": "KES",
        "country": "KE",
        "paymentReference": "643108207791261657324A3",
        "email": "test@yourdomain.com",
        "productId": "productID",
        "productDescription": "WEIGHING AND ADMIN CHARGES",
        "callbackUrl": "http://yourdomain.com",
        "hash": hash_str,
        "hashType": "sha256"
    }
    json_response = standard_checkout_service.initialize_transaction(standard_checkout_payload)
    print("================== stop initialize transaction ==================")
    return json_response


token = authenticate()

if token:
    print("standard checkout response: " + str(initialize_transaction(token)))
else:
    print("authentication failure")
