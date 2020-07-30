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
from requests import Response


class SeerbitError(RuntimeError):

    def __init__(self, message=""):
        self.message = message
        super(SeerbitError, self).__init__(message)

    @staticmethod
    def handle_error(response: Response):
        json_object = response.json()
        error_message = "{0}: {1}"
        if json_object.get("status") and json_object.get("data"):
            status = json_object["status"]
            if status.lower() == "error":
                raise SeerbitError(json_object["data"]["message"])
        if json_object.get("message") and json_object.get("errorCode"):
            error_message = error_message.format(str(json_object["message"]), str(json_object["errorCode"]))
            print(error_message)
            raise SeerbitError(str(json_object["message"]))
        elif json_object["message"]:
            raise SeerbitError(json_object["message"])
        else:
            raise SeerbitError("Unknown Error")


class SeerbitConnectionError(RuntimeError):

    def __init__(self, message="", code=0, status=None, timestamp=None):
        self.message = message
        self.code = code
        self.status = status
        self.timestamp = timestamp
        super(SeerbitConnectionError, self).__init__(message, code, status, timestamp)
