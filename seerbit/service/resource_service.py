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
from seerbit.interface.service_interface import IResourceService
from seerbit.service.servicelib import Service
from seerbit.utility import Utility


class ResourceService(Service, IResourceService, IClientConstants):

    def __init__(self, client: Client, token: str):
        """
        :param Client client:
            A non optional Client, the client with config

        :param str token:
            A non optional string, the auth token

        """
        super(ResourceService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def get_bank_list(self, public_key: str):
        """

        GET /banks/merchant/{public_key}

        :param str public_key:
            A non optional string, the merchant public key

        """
        self.requires_token = True
        endpoint = IClientConstants.BANK_LIST_ENDPOINT.format(public_key)
        self.response = self.get_request(endpoint, self.token)
        return self.response
