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
from seerbit.service.account_service import AccountService
from seerbit.service.authentication import Authentication

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


def authorize(token_str: str):
    """ account authorization """
    print("================== start account authorization ==================")
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    account_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "fee": "10",
        "fullName": "John Doe",
        "mobileNumber": "08037456590",
        "currency": "NGN",
        "country": "NG",
        "paymentReference": payment_ref,
        "email": "johndoe@gmail.com",
        "productId": "Foods",
        "productDescription": "Uba Account Transaction ",
        "clientAppCode": "kpp64",
        "channelType": "BANK_ACCOUNT",
        "redirectUrl": "https://checkout.seerbit.com",
        "deviceType": "Apple Laptop",
        "sourceIP": "127.0.0.1:3456",
        "accountName": "John S Doe",
        "accountNumber": "1234567890",
        "bankCode": "033",
        "bvn": "12345678901",
        "dateOfBirth": "04011984",
        "retry": "false",
        "invoiceNumber": "1234567891abc123ac"
    }
    account_service = AccountService(client, token_str)
    json_response = account_service.authorize(account_payload)
    print("================== stop account authorization ==================")
    return json_response


token = authenticate()

if token:
    print("account authorize response: " + str(authorize(token)))
else:
    print("authentication failure")
