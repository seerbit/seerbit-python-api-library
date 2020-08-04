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


class INumericConstants(object):
    # numeric constants
    MIN_VALUE = 1
    MIN_SIZE = 1
    NIL = 0
    HTTP_STATUS_200 = 200
    HTTP_STATUS_299 = 299


class ISeerbit(object):

    @property
    def api_version(self):
        raise NotImplementedError

    @api_version.setter
    def api_version(self, api_version):
        pass

    @property
    def live_api_base(self):
        raise NotImplementedError

    @property
    def test_api_base(self):
        raise NotImplementedError


class IConfig(object):
    data = {}

    def get(self, key):
        pass

    @property
    def public_key(self):
        raise NotImplementedError

    @property
    def private_key(self):
        raise NotImplementedError

    def put(self, key, value):
        pass

    @property
    def timeout(self):
        raise NotImplementedError


class IClientConstants(object):
    # base url
    TEST_API_BASE = "https://pilot-backend.seerbitapi.com/"
    LIVE_API_BASE = "https://seerbitapi.com/"

    # authentication
    AUTHENTICATION_ENDPOINT = "api/v2/encrypt/keys"
    HASH_REQUEST = "api/v2/encrypt/hashs"

    # bank & card payment options
    INITIALIZE_TRANSACTIONS = "api/v2/payments"
    INITIATE_PAYMENT_ENDPOINT = "api/v2/payments/initiates"
    VALIDATE_PAYMENT_ENDPOINT = "api/v2/payments/validate"
    VALIDATE_CARD_PAYMENT_ENDPOINT = "api/v2/payments/otp"
    PREAUTH_AUTHORIZE_ENDPOINT = "api/v2/payments/authorise"
    PAYMENT_CAPTURE_ENDPOINT = "api/v2/payments/capture"
    PAYMENT_REFUND_ENDPOINT = "api/v2/payments/refund"
    PAYMENT_CANCEL_ENDPOINT = "api/v2/payments/cancel"
    PAYMENT_CHARGE_ENDPOINT = "api/v2/payments/charge"
    TOKENIZATION_ENDPOINT = "api/v2/payments/tokenize"

    # refunds
    REFUND_ENDPOINT = "merchants/api/v1/user/{0}/refunds"
    REFUND_DETAIL_ENDPOINT = "merchants/api/v1/user/{0}/refunds/{1}"
    REFUND_LIST_ENDPOINT = "merchants/api/v1/user/{0}/refunds?page={1}&size={2}"

    # orders
    ORDERS_ENDPOINT = "api/v2/payments/order"

    # mobile money
    AVAILABLE_NETWORKS_ENDPOINT = "api/v2/networks"

    # recurring
    SUBSCRIPTION_ENDPOINT = "api/v2/recurring/subscribes"
    CUSTOMER_SUBSCRIPTION_ENDPOINT = "api/v2/recurring/{0}/customerId/{1}"
    UPDATE_SUBSCRIPTION_ENDPOINT = "api/v2/recurring/updates"
    MERCHANT_SUBSCRIPTIONS_ENDPOINT = "api/v2/recurring/publicKey/{0}"
    CHARGE_ENDPOINT = "api/v2/recurring/charge"

    # status queries
    TRX_STATUS_ENDPOINT = "api/v2/payments/query/{0}"
    SUBSCRIPTION_STATUS_ENDPOINT = "api/v2/recurring/billingId/{0}"

    # bank list
    BANK_LIST_ENDPOINT = "api/v2/banks/merchant/{0}"

    # version types
    VERSION_ONE = "1.0.0"
    VERSION_TWO = "1.0.1"


class IHttpClient(object):

    def post(self, service, request_url, params, token):
        pass

    def put(self, service, request_url, params, token):
        pass

    def get(self, service, request_url, token):
        pass
