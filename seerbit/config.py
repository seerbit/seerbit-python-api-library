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
from seerbit.interface.app_interface import IConfig, INumericConstants


class Config(IConfig, INumericConstants):

    @property
    def timeout(self):
        return self.timeout

    def get(self, key: str):
        return Config.data[key] if Config.data is not None else None

    @property
    def public_key(self) -> str:
        public_key = ""
        if len(Config.data) != 0:
            public_key = Config.data.get("public_key")
        return public_key

    @property
    def private_key(self) -> str:
        private_key = ""
        if len(Config.data) != 0:
            private_key = Config.data.get("private_key")
        return private_key

    def put(self, key, value):
        Config.data[key] = value

