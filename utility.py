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
from client import Client
from exception import SeerbitException


class Utility:

    @staticmethod
    def non_null(client: Client):
        if not client:
            raise SeerbitException("Client cannot be null")
        if not client.config().get_private_key():
            raise SeerbitException("private key is required")
        if not client.config().get_public_key():
            raise SeerbitException("public key is required")

    @staticmethod
    def require_non_null(api_base, error_message):
        if not api_base:
            raise SeerbitException(error_message)
