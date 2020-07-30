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
from seerbit.service.card_service import CardService

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


def card_validate_otp(token_str: str):
    """ Initiate Card Payment """
    print("================== start card otp validate ==================")
    card_otp_payload = {
        "transaction": {
            "linkingreference": "F736308021578652945922",
            "otp": "410303"
        }
    }
    card_service = CardService(client, token_str)
    json_response = card_service.validate(card_otp_payload)
    print("================== stop card otp validate ==================")
    return json_response


token = authenticate()

if token:
    print("card otp validate response: " + str(card_validate_otp(token)))
else:
    print("authentication failure")
