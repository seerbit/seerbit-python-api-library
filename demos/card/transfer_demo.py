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
from seerbit.service.transfer_service import TransferService

client = Client()


def transfer(token_str: str):
    """ Initiate Transfer """
    print("================== start transfer ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    transfer_payload = {
        "paymentReference": payment_ref,
        "publicKey": client.public_key,
        "currency": "NGN",
        "country": "NG",
        "amount": "100.00",
        "email": "johndoe@gmail.com",
        "fullName": "john doe",
        "paymentType": "TRANSFER",
        "mobileNumber": "08087522256",
        "callbackUrl": "http://checkout-seerbit.surge.sh",
        "redirectUrl": "http://checkout-seerbit.surge.sh"
    }
    transfer_service = TransferService(client, token_str)
    json_response = transfer_service.payment_transfer(transfer_payload)
    print("================== stop transfer ==================")
    return json_response


client.api_base = SeerBit.LIVE_API_BASE
client.environment = EnvironmentEnum.LIVE.value
client.private_key = "private_key"
client.public_key = "public_key"
client.timeout = 20
auth_service = Authentication(client)
auth_service.auth()
token = auth_service.get_token()

if token:
    print("transfer response: " + str(transfer(token)))
else:
    print("authentication failure")
