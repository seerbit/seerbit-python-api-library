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
from seerbit.interface.app_interface import IClientConstants
from seerbit.interface.service_interface import IMobileMoneyService
from seerbit.service.servicelib import Service
from seerbit.validation import MobileMoneyValidator
from seerbit.utility import Utility


class MobileMoneyService(Service, IMobileMoneyService, IClientConstants):

    def __init__(self, client: Client, token: str):
        """

        :param Client client:
            A non optional Client, the client with config

        :param str token:
            A non optional string, the auth token

        """
        super(MobileMoneyService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def authorize(self, mobile_money: dict):
        """

        POST /api/v2/payments/initiates

        :param dict mobile_money:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        MobileMoneyValidator.is_valid_authorize(schema=mobile_money)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, mobile_money, self.token)
        return self.response

    def get_available_networks(self):
        """

        GET /api/v2/networks

        :returns Any self.response

        """
        self.requires_token = True
        return self.get_request(IClientConstants.AVAILABLE_NETWORKS_ENDPOINT, self.token)
