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


# request
class IRequest(object):

    def post_request(self, endpoint, payload, token):
        pass

    def put_request(self, endpoint, payload, token):
        pass

    def get_request(self, endpoint, token):
        pass


class IService(object):

    @property
    def client(self):
        raise NotImplementedError

    @property
    def requires_token(self):
        raise NotImplementedError

    @requires_token.setter
    def requires_token(self, is_required):
        pass


# account service
class IAccountService(object):

    def authorize(self, payload):
        pass

    def validate(self, payload):
        pass


# auth service
class IAuthentication(object):

    def auth(self):
        pass

    def get_token(self) -> str:
        pass


# card service
class ICardService(object):

    def authorize(self, card: dict):
        pass

    def validate(self, transaction: dict):
        pass

    def preauth_authorization(self, card_pre_auth: dict):
        pass

    def payment_capture(self, payment_capture: dict):
        pass

    def payment_refund(self, payment_refund: dict):
        pass

    def payment_cancel(self, payment_cancel: dict):
        pass

    def payment_charge_non3d(self, payment_charge: dict):
        pass

    def payment_charge_3ds(self, payment_charge: dict):
        pass

    def payment_charge_3d(self, payment_charge: dict):
        pass

    def tokenize(self, payment_charge: dict):
        pass


# mobile money service
class IMobileMoneyService(object):

    def authorize(self, mobile_money):
        pass

    def get_available_networks(self):
        pass


# order service
class IOrderService(object):

    def authorize(self, card):
        pass


# resource service
class IResourceService(object):

    def get_bank_list(self, public_key):
        pass


# status service
class IStatusService(object):

    def get_transaction_status(self, payment_reference):
        pass

    def get_subscription_status(self, billing_id):
        pass


# recurrent service
class IRecurringService(object):

    def create_subscription(self, subscription):
        pass

    def get_customer_subscriptions(self, public_key, customer_id):
        pass

    def update_subscription(self, subscription: dict):
        pass

    def get_merchant_subscriptions(self, public_key):
        pass

    def recurring_debit(self, recurring_debit: dict):
        pass


# refund service
class IRefundService(object):

    def all_refunds(self, business_id, page, size):
        pass

    def get_refund(self, business_id, refund_id):
        pass

    def refund(self, business_id, payload):
        pass


# standard checkout service
class IStandardCheckoutService(object):

    def initialize_transaction(self, standard_checkout: dict):
        pass

    def get_hash(self, standard_checkout: dict) -> str:
        pass
