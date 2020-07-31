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
from seerbit.enums import EnvironmentEnum, AuthTypeEnum
from seerbit.seerbitlib import Seerbit
from seerbit.service.authentication import Authentication
from seerbit.service.card_service import CardService

client = Client()


def card_tokenize(token_str: str):
    """ Initiate Card Tokenize """
    print("================== start card tokenize ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    card_payload = {
        "publicKey": client.public_key,
        "fullName": "john doe",
        "mobileNumber": "08033456599",
        "currency": "NGN",
        "country": "NG",
        "email": "johndoe@gmail.com",
        "productId": "Foods",
        "productDescription": "Test Description",
        "cardNumber": "5123450000000008",
        "cvv": "100",
        "expiryMonth": "05",
        "expiryYear": "21",
        "pin": "1234",
        "paymentReference": payment_ref
    }
    card_service = CardService(client, token_str)
    json_response = card_service.tokenize(card_payload)
    print("================== stop card tokenize ==================")
    return json_response


client.api_base = Seerbit.LIVE_API_BASE
client.environment = EnvironmentEnum.LIVE.value
client.private_key = "private_key"
client.public_key = "public_key"
client.timeout = 20
client.authentication_scheme = AuthTypeEnum.BASIC.value
auth_service = Authentication(client)
token = auth_service.get_basic_auth_encoded_string()

if token:
    print("card tokenize response: " + str(card_tokenize(token)))
else:
    print("authentication failure")
