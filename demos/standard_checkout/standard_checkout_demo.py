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
import hashlib

from seerbit.client import Client
from seerbit.enums import EnvironmentEnum
from seerbit.seerbitlib import Seerbit
from seerbit.service.authentication import Authentication
from seerbit.service.standard_checkout_service import StandardCheckoutService

client = Client()


def authenticate() -> str:
    """ User authentication token """
    print("================== start authentication ==================")
    client.api_base = Seerbit.LIVE_API_BASE
    client.environment = EnvironmentEnum.LIVE.value
    client.private_key = "SBTESTSECK_kFgKytQK1KSvbR616rUMqNYOUedK3Btm5igZgxaZ"
    client.public_key = "SBTESTPUBK_p8GqvFSFNCBahSJinczKd9aIPoRUZfda"
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
        "currency": "NGN",
        "country": "NG",
        "paymentReference": "643108207791261657324A3A",
        "email": "test@yourdomain.com",
        "productId": "productID",
        "productDescription": "WEIGHING AND ADMIN CHARGES",
        "callbackUrl": "http://yourdomain.com"
    }
    hash_str = standard_checkout_service.get_hash(hash_payload)
    standard_checkout_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "currency": "NGN",
        "country": "NG",
        "paymentReference": "643108207791261657324A3A",
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


def sha256(hash_string: str) -> str:
    """ Build Hash Signature """
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def initialize_transaction_with_manual_hash(token_str: str):
    """ Initialize Transaction With Manual Hash """
    print("================== start initialize transaction ==================")
    standard_checkout_service = StandardCheckoutService(client, token_str)
    hash_payload = 'amount=100.00&callbackUrl=http://yourdomain.com&country=NG&currency=NGN' \
                   + '&email=test@yourdomain.com&paymentReference=643108207791261657324A333' \
                   + '&productDescription=WEIGHING AND ADMIN CHARGES&productId=productID&publicKey=' \
                   + client.public_key + client.private_key
    hash_str = sha256(hash_payload)
    standard_checkout_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "currency": "NGN",
        "country": "NG",
        "paymentReference": "643108207791261657324A333",
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
    print("standard checkout response (manual hash): " + str(initialize_transaction_with_manual_hash(token)))
else:
    print("authentication failure")
