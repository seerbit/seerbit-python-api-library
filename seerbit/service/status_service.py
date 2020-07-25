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
from seerbit.interface.service_interface import IStatusService
from seerbit.service.servicelib import Service
from seerbit.utility import Utility


class StatusService(Service, IStatusService, IClientConstants):

    def __init__(self, client, token):
        super(StatusService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def get_transaction_status(self, payment_reference):
        """ GET /api/v2/payments/query/{payment_reference} """
        self.requires_token = True
        endpoint = IClientConstants.TRX_STATUS_ENDPOINT.format(payment_reference)
        self.response = self.get_request(endpoint, self.token)
        return self.response

    def get_subscription_status(self, billing_id):
        """ GET /api/v2/recurring/billingId/{billing_id} """
        self.requires_token = True
        endpoint = IClientConstants.SUBSCRIPTION_STATUS_ENDPOINT.format(billing_id)
        self.response = self.get_request(endpoint, self.token)
        return self.response
