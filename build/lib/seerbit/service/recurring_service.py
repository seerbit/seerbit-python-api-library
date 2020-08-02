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
from seerbit.interface.service_interface import IRecurringService
from seerbit.service.servicelib import Service
from seerbit.utility import Utility
from seerbit.validation import RecurringValidator


class RecurringService(Service, IRecurringService, IClientConstants):

    def __init__(self, client: Client, token: str):
        """

        :param Client client:
            A non optional Client, the client with config

        :param str token:
            A non optional string, the auth token

        """
        super(RecurringService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def create_subscription(self, subscription: dict):
        """

        POST /api/v2/recurring/subscribes

        :param dict subscription:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        RecurringValidator.is_valid_create_subscription(schema=subscription)
        self.response = self.post_request(IClientConstants.SUBSCRIPTION_ENDPOINT, subscription, self.token)
        return self.response

    def get_customer_subscriptions(self, public_key: str, customer_id: str):
        """

        GET /api/v2/recurring/{public_key}/customerId/{customer_id}

        :param str public_key:
            A non optional string, the merchant public key

        :param str customer_id:
            A non optional string, the customer id

        :returns Any self.response

        """
        self.requires_token = True
        endpoint = IClientConstants.CUSTOMER_SUBSCRIPTION_ENDPOINT.format(public_key, customer_id)
        self.response = self.get_request(endpoint, self.token)
        return self.response

    def update_subscription(self, subscription: dict):
        """
        PUT /api/v2/recurring/updates

        :param dict subscription:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        RecurringValidator.is_valid_update_subscription(schema=subscription)
        self.response = self.put_request(IClientConstants.UPDATE_SUBSCRIPTION_ENDPOINT, subscription, self.token)
        return self.response

    def get_merchant_subscriptions(self, public_key: str):
        """

        GET /api/v2/recurring/publicKey/{public_key}

        :param str public_key:
            A non optional string, the merchant public key

        :returns Any self.response

        """
        self.requires_token = True
        endpoint = IClientConstants.MERCHANT_SUBSCRIPTIONS_ENDPOINT.format(public_key)
        self.response = self.get_request(endpoint, self.token)
        return self.response

    def recurring_debit(self, recurring_debit: dict):
        """

        POST /api/v2/recurring/charge

        :param dict recurring_debit:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        RecurringValidator.is_valid_recurring_debit(schema=recurring_debit)
        self.response = self.post_request(IClientConstants.CHARGE_ENDPOINT, recurring_debit, self.token)
        return self.response
