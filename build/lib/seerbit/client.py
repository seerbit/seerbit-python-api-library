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
from seerbit.config import Config
from seerbit.interface.app_interface import IClientConstants
from seerbit.enums import EnvironmentEnum, AuthTypeEnum
from seerbit.exception import SeerbitError


class Client:

    def __init__(self, version=None):
        self.config = Config()
        self.config.put("authentication_scheme", str(AuthTypeEnum.BEARER.value))
        if version is None:
            self.config.put("version", IClientConstants.VERSION_TWO)
        else:
            if "1.0.1" == version:
                self.config.put("version", IClientConstants.VERSION_TWO)
            else:
                raise SeerbitError("Version must be \"1.0.1\"")

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config: Config):
        self._config = config

    @property
    def public_key(self):
        return self._config.get("public_key")

    @public_key.setter
    def public_key(self, public_key: str):
        self._config.put("public_key", public_key)

    @property
    def private_key(self):
        return self._config.get("private_key")

    @private_key.setter
    def private_key(self, public_key: str):
        self._config.put("private_key", public_key)

    @property
    def version(self):
        return str(self._config.get("version"))

    @version.setter
    def version(self, version: str):
        if "1.0.1" == version:
            self._config.put("version", IClientConstants.VERSION_TWO)
        else:
            raise SeerbitError("Version must be \"1.0.1\"")

    @property
    def environment(self):
        env = ""
        if self.config.get("environment") is not None:
            env = str(self.config.get("environment"))
        return env

    @environment.setter
    def environment(self, environment: str):
        if environment == str(EnvironmentEnum.LIVE.value):
            self._config.put("environment", str(EnvironmentEnum.LIVE.value))
            self._config.put("api_base", IClientConstants.LIVE_API_BASE)
        elif environment == str(EnvironmentEnum.TEST.value):
            self._config.put("environment", str(EnvironmentEnum.TEST.value))
            self._config.put("api_base", IClientConstants.TEST_API_BASE)
        else:
            msg = "This environment does not exist, use \"{0}\" or \"{1}\""
            error_message = msg.format(EnvironmentEnum.LIVE.value, EnvironmentEnum.TEST.value)
            raise SeerbitError(error_message)

    @property
    def authentication_scheme(self):
        auth_type: str = ""
        if self.config.get("authentication_scheme") is not None:
            auth_type = str(self.config.get("authentication_scheme"))
        return auth_type

    @authentication_scheme.setter
    def authentication_scheme(self, auth_type: str):
        auth_type: str = auth_type.lower()
        if auth_type in ["basic ", "bearer "]:
            self.config.put("authentication_scheme", auth_type)
        else:
            raise SeerbitError("Invalid Authentication Scheme")

    @property
    def api_base(self):
        return str(self._config.get("api_base"))

    @api_base.setter
    def api_base(self, api_base: str):
        self._config.put("api_base", api_base)

    @property
    def timeout(self):
        return self._config.get("timeout")

    @timeout.setter
    def timeout(self, timeout):
        self._config.put("timeout", timeout)
