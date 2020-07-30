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
from seerbit.enums import EnvironmentEnum, AuthTypeEnum
from seerbit.seerbitlib import Seerbit
from seerbit.service.authentication import Authentication
from seerbit.service.card_service import CardService

client = Client()


def card_payment_capture(token_str: str):
    """ Initiate Card Payment Capture """
    print("================== start card payment capture ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    card_payload = {
        "paymentReference": payment_ref,
        "publicKey": client.public_key,
        "currency": "KES",
        "country": "KE",
        "productDescription": "test capture",
        "amount": "100.00"
    }
    card_service = CardService(client, token_str)
    json_response = card_service.payment_capture(card_payload)
    print("================== stop card payment capture ==================")
    return json_response


client.api_base = Seerbit.LIVE_API_BASE
client.environment = EnvironmentEnum.LIVE.value
config = Config()
config.put("public_key", "SBTESTPUBK_E9CFg6iZ2uSFr8YK7C2KTontiysQRnMm")
config.put("private_key", "SBTESTSECK_V1ahfeTQAsyi3OaJXbMmrKNB8KTW5dyCRdUnILnw")
client.config = config
client.timeout = 20
client.authentication_scheme = AuthTypeEnum.BASIC.value
auth_service = Authentication(client)
token = auth_service.get_basic_auth_encoded_string()
if token:
    print("card capture payment response: " + str(card_payment_capture(token)))
else:
    print("authentication failure")
