"""
  Copyright (C) 2022 SeerBit

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
from seerbit.seerbitlib import SeerBit
from seerbit.service.authentication import Authentication
from seerbit.service.card_service import CardService

client = Client()


def authenticate() -> str:
    """ User authentication token """
    print("================== start authentication ==================")
    client.api_base = SeerBit.LIVE_API_BASE
    client.environment = EnvironmentEnum.LIVE.value
    client.private_key = "private_key"
    client.public_key = "public_key"
    client.timeout = 20
    auth_service = Authentication(client)
    auth_service.auth()
    print("================== stop authentication ==================")
    return auth_service.get_token()


def card_3ds_charge(token_str: str):
    """ Initiate Card 3DS Charge """
    print("================== start card 3ds charge ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    card_payload = {
        "publicKey": client.public_key,
        "amount": "1000.00",
        "fee": "10",
        "fullName": "Victor Ighalo",
        "mobileNumber": "08032000033",
        "currency": "NGN",
        "country": "NG",
        "paymentReference": payment_ref,
        "email": "johndoe@gmail.com",
        "productId": "Foods",
        "productDescription": "Test Description",
        "clientAppCode": "kpp64",
        "redirectUrl": "www.ser1.com",
        "channelType": "Mastercard",
        "deviceType": "Apple Laptop",
        "sourceIP": "127.0.0.1:3456",
        "cardNumber": "5123450000000008",
        "cvv": "100",
        "expiryMonth": "05",
        "expiryYear": "21",
        "pin": "####",
        "retry": "false",
        "paymentType": "CARD",
        "invoiceNumber": "1234567890abc123ac"
    }
    card_service = CardService(client, token_str)
    json_response = card_service.payment_charge_3ds(card_payload)
    print("================== stop card 3ds charge ==================")
    return json_response


token = authenticate()

if token:
    print("card non 3d charge response: " + str(card_3ds_charge(token)))
else:
    print("authentication failure")
