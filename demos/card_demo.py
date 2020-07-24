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
from client import Client
from config import Config
from enums import EnvironmentEnum
from seerbit import Seerbit
from service.account_service import AccountService
from service.authentication import Authentication
from service.card_service import CardService

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


def card_authorize(token_str: str):
    """ Initiate Card Payment """
    print("================== start card authorize ==================")
    random_number = randint(0, 16777215)
    payment_ref = str(hex(random_number))
    card_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "fee": "10",
        "fullName": "Peter Diei",
        "mobileNumber": "08030540611",
        "currency": "NGN",
        "country": "NG",
        "paymentReference": payment_ref,
        "email": "okechukwu.diei2@gmail.com",
        "productId": "product101",
        "productDescription": "ONE WORLD",
        "clientAppCode": "kpp64",
        "redirectUrl": "http://checkout-seerbit.surge.sh",
        "paymentType": "CARD",
        "scheduleId": "",
        "channelType": "Mastercard",
        "deviceType": "Apple Laptop",
        "sourceIP": "127.0.0.1:3456",
        "cardNumber": "2223000000000007",
        "cvv": "100",
        "expiryMonth": "05",
        "expiryYear": "37",
        "pin": "1234",
        "type": "3DSECURE",
        "retry": "false",
        "invoiceNumber": "1234567890abc123ac"
    }
    card_service = CardService(client, token_str)
    json_response = card_service.authorize(card_payload)
    print("================== stop card authorize ==================")
    return json_response


token = authenticate()

if token:
    print("card authorize response: " + str(card_authorize(token)))
else:
    print("authentication failure")
