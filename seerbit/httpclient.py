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
from seerbit.interface.app_interface import IHttpClient, INumericConstants
from seerbit.enums import HttpHeaderEnum
from seerbit.exception import SeerbitConnectionError, SeerbitError
from requests import post, get, put


class HttpClient(IHttpClient, INumericConstants):

    def __init__(self):
        self.status_code = -20

    def post(self, service, request_url, params, token):
        client = service.client
        if service.requires_token:
            if not token or len(token) < self.MIN_SIZE:
                raise SeerbitConnectionError("Please provide an authentication token.")
            else:
                authentication_scheme = client.authentication_scheme
                if authentication_scheme.lower() == "basic ":
                    token = "Basic {0}".format(token)
                elif authentication_scheme.lower() == "bearer ":
                    token = "Bearer {0}".format(token)
                else:
                    raise SeerbitError("Invalid Authentication Scheme")
                header = {
                    "Authorization": token,
                    "Request-Timeout": str(service.client.timeout),
                    str(HttpHeaderEnum.CONTENT_TYPE_PARAM.value): str(HttpHeaderEnum.CONTENT_TYPE_VALUE.value)
                }
                response = post(url=request_url, json=params, headers=header)
        else:
            header = {
                "Request-Timeout": str(service.client.timeout),
                str(HttpHeaderEnum.CONTENT_TYPE_PARAM.value): str(HttpHeaderEnum.CONTENT_TYPE_VALUE.value)
            }
            response = post(url=request_url, json=params, headers=header)
        status_code = int(response.status_code)
        if status_code < self.HTTP_STATUS_200 or status_code > self.HTTP_STATUS_299:
            SeerbitError.handle_error(response)
        return response

    def put(self, service, request_url, params, token):
        client = service.client
        if service.requires_token:
            if not token or len(token) < self.MIN_SIZE:
                raise SeerbitConnectionError("Please provide an authentication token.")
            else:
                authentication_scheme = client.authentication_scheme
                if authentication_scheme.lower() == "basic ":
                    token = "Basic {0}".format(token)
                elif authentication_scheme.lower() == "bearer ":
                    token = "Bearer {0}".format(token)
                else:
                    raise SeerbitError("Invalid Authentication Scheme")
                header = {
                    "Authorization": token,
                    "Request-Timeout": str(service.client.timeout),
                    str(HttpHeaderEnum.CONTENT_TYPE_PARAM): str(HttpHeaderEnum.CONTENT_TYPE_VALUE)
                }
                response = put(url=request_url, json=params, headers=header)
        else:
            header = {
                str(HttpHeaderEnum.CONTENT_TYPE_PARAM.value): str(HttpHeaderEnum.CONTENT_TYPE_VALUE.value),
                "Request-Timeout": str(service.client.timeout)
            }
            response = put(url=request_url, json=params, headers=header)
        status_code = int(response.status_code)
        if status_code < self.HTTP_STATUS_200 or status_code > self.HTTP_STATUS_299:
            SeerbitError.handle_error(response)
        return response

    def get(self, service, request_url, token):
        client = service.client
        if service.requires_token:
            if not token or len(token) < self.MIN_SIZE:
                raise SeerbitConnectionError("Please provide an authentication token.")
            else:
                authentication_scheme = client.authentication_scheme
                if authentication_scheme.lower() == "basic ":
                    token = "Basic {0}".format(token)
                elif authentication_scheme.lower() == "bearer ":
                    token = "Bearer {0}".format(token)
                else:
                    raise SeerbitError("Invalid Authentication Scheme")
                header = {
                    "Authorization": token,
                    "Request-Timeout": str(service.client.timeout),
                    str(HttpHeaderEnum.CONTENT_TYPE_PARAM.value): str(HttpHeaderEnum.CONTENT_TYPE_VALUE.value)
                }
                response = get(url=request_url, headers=header)
        else:
            header = {
                str(HttpHeaderEnum.CONTENT_TYPE_PARAM.value): str(HttpHeaderEnum.CONTENT_TYPE_VALUE.value),
                "Request-Timeout": str(service.client.timeout)
            }
            response = get(url=request_url, headers=header)
        status_code = int(response.status_code)
        if status_code < self.HTTP_STATUS_200 or status_code > self.HTTP_STATUS_299:
            SeerbitError.handle_error(response)
        return response
