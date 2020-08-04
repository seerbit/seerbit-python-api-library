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
from seerbit.exception import SeerbitError
from seerbit.interface.app_interface import IClientConstants
from seerbit.interface.service_interface import IStandardCheckoutService
from seerbit.service.servicelib import Service
from seerbit.utility import Utility
from seerbit.validation import StandardCheckoutValidator


class StandardCheckoutService(Service, IStandardCheckoutService, IClientConstants):

    def __init__(self, client: Client, token: str):
        """

        :param Client client:
            A non optional Client, the client with config

        :param str token:
            A non optional string, the auth token

        """
        super(StandardCheckoutService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def initialize_transaction(self, standard_checkout: dict):
        """

        POST /api/v2/payments

        :param dict standard_checkout:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        StandardCheckoutValidator.is_valid_checkout(schema=standard_checkout)
        endpoint = IClientConstants.INITIALIZE_TRANSACTIONS
        self.response = self.post_request(endpoint, standard_checkout, self.token)
        return self.response

    def get_hash(self, standard_checkout: dict) -> str:
        """

        POST /api/v2/encrypt/hashs

        :param dict standard_checkout:
            A non optional dict, the payload

        :returns str hash_str

        """
        self.requires_token = True
        StandardCheckoutValidator.is_valid_checkout(schema=standard_checkout)
        response = self.post_request(IClientConstants.HASH_REQUEST, standard_checkout, self.token)
        if response.get("data"):
            response = response.get("data")
            if response.get("hash"):
                hash_str = response["hash"]["hash"]
            else:
                raise SeerbitError("Unable to obtain hash")
        else:
            raise SeerbitError("Unable to obtain hash")
        return hash_str
