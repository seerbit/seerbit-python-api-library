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
from seerbit.interface.app_interface import ISeerbit, IClientConstants


class Seerbit(ISeerbit, IClientConstants):

    @property
    def api_version(self):
        return self.api_version

    @api_version.setter
    def api_version(self, api_version):
        self.api_version = api_version

    @property
    def live_api_base(self):
        return self.LIVE_API_BASE

    @property
    def test_api_base(self):
        return self.TEST_API_BASE

