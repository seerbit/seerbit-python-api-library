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
from interface.app_interface import IClientConstants
from interface.service_interface import IAccountService
from service.service import Service
from validation import AccountValidator
from utility import Utility


class AccountService(Service, IAccountService, IClientConstants):

    def __init__(self, client, token):
        super(AccountService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def authorize(self, account_payload: dict):
        """POST /api/v2/payments/initiates"""
        AccountValidator.is_valid_authorize(payload=account_payload)
        self.requires_token = True
        client = self.client
        account_payload.update({"publicKey": client.public_key})
        response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, account_payload, self.token)
        return response

    def validate(self, otp_payload: dict):
        """POST /api/v2/payments/validate"""
        AccountValidator.is_valid_validate(payload=otp_payload)
        self.requires_token = True
        response = self.post_request(IClientConstants.VALIDATE_PAYMENT_ENDPOINT, otp_payload, self.token)
        return response
