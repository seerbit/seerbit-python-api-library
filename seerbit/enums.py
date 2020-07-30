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
from enum import Enum


class EnvironmentEnum(Enum):
    TEST = "test"
    LIVE = "live"


class RefundType(Enum):
    FULL_REFUND = "FULL_REFUND"
    PARTIAL_REFUND = "PARTIAL_REFUND"


class HttpHeaderEnum(Enum):
    CONTENT_TYPE_PARAM = "Content-Type"
    CONTENT_TYPE_VALUE = "application/json"


class AuthTypeEnum(Enum):
    BASIC = "Basic "
    BEARER = "Bearer "
