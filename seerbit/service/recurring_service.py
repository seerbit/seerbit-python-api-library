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
from seerbit.interface.app_interface import IClientConstants
from seerbit.interface.service_interface import IRecurringService
from seerbit.service.servicelib import Service
from seerbit.utility import Utility
from seerbit.validation import RecurringValidator


class RecurringService(Service, IRecurringService, IClientConstants):

    def __init__(self, client, token):
        super(RecurringService, self).__init__(client, token)
        self.token = token
        Utility.non_null(client)

    def create_subscription(self, subscription):
        """ POST /api/v2/recurring/subscribes """
        self.requires_token = True
        RecurringValidator.is_valid_create_subscription(payload=subscription)
        self.response = self.post_request(IClientConstants.SUBSCRIPTION_ENDPOINT, subscription, self.token)
        return self.response

    def get_customer_subscriptions(self, public_key, customer_id):
        """ GET /api/v2/recurring/{public_key} """
        self.requires_token = True
        self.response = self.get_request(IClientConstants.CUSTOMER_SUBSCRIPTION_ENDPOINT, public_key, self.token)
        return self.response

    def update_subscription(self, subscription):
        """ POST /api/v2/recurring/updates """
        self.requires_token = True
        RecurringValidator.is_valid_update_subscription(payload=subscription)
        self.response = self.post_request(IClientConstants.UPDATE_SUBSCRIPTION_ENDPOINT, subscription, self.token)
        return self.response

    def get_merchant_subscriptions(self, public_key):
        pass

    def recurring_debit(self, recurring_debit):
        """ POST /api/v2/recurring/charge """
        self.requires_token = True
        RecurringValidator.is_valid_recurring_debit(payload=recurring_debit)
        self.response = self.post_request(IClientConstants.CHARGE_ENDPOINT, recurring_debit, self.token)
        return self.response
