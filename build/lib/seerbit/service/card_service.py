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
from seerbit.interface.service_interface import ICardService
from seerbit.service.servicelib import Service
from seerbit.validation import CardValidator
from seerbit.utility import Utility


class CardService(Service, ICardService, IClientConstants):

    def __init__(self, client: Client, token: str):
        """

        :param Client client:
            A non optional Client, the client with config

        :param str token:
            A non optional string, the auth token

        """
        super().__init__(client)
        self.token = token
        Utility.non_null(client)

    def authorize(self, card: dict):
        """

        POST /api/v2/payments/initiates

        :param dict card:
            A non optional dict, the payment

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_authorize(schema=card)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, card, self.token)
        return self.response

    def validate(self, otp: dict):
        """

        POST /api/v2/payments/otp

        :param dict otp:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_validate(schema=otp)
        self.response = self.post_request(IClientConstants.VALIDATE_CARD_PAYMENT_ENDPOINT, otp, self.token)
        return self.response

    def preauth_authorization(self, card_pre_auth: dict):
        """

        POST /api/v2/payments/authorise

        :param dict card_pre_auth:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_preauth(schema=card_pre_auth)
        self.response = self.post_request(IClientConstants.PREAUTH_AUTHORIZE_ENDPOINT, card_pre_auth, self.token)
        return self.response

    def payment_capture(self, payment_capture: dict):
        """

        POST /api/v2/payments/capture

        :param dict payment_capture:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_payment_capture(schema=payment_capture)
        self.response = self.post_request(IClientConstants.PAYMENT_CAPTURE_ENDPOINT, payment_capture, self.token)
        return self.response

    def payment_refund(self, payment_refund: dict):
        """

        POST /api/v2/payments/refund

        :param dict payment_refund:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_payment_refund(schema=payment_refund)
        self.response = self.post_request(IClientConstants.PAYMENT_REFUND_ENDPOINT, payment_refund, self.token)
        return self.response

    def payment_cancel(self, payment_cancel: dict):
        """

        POST /api/v2/payments/cancel

        :param dict payment_cancel:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_payment_cancel(schema=payment_cancel)
        self.response = self.post_request(IClientConstants.PAYMENT_CANCEL_ENDPOINT, payment_cancel, self.token)
        return self.response

    def payment_charge_non3d(self, payment_charge: dict):
        """

        POST /api/v2/payments/charge

        :param dict payment_charge:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_payment_charge_non3d(schema=payment_charge)
        self.response = self.post_request(IClientConstants.PAYMENT_CHARGE_ENDPOINT, payment_charge, self.token)
        return self.response

    def payment_charge_3ds(self, payment_charge: dict):
        """

        POST /api/v2/payments/initiates

        :param dict payment_charge:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_payment_charge_3ds(schema=payment_charge)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, payment_charge, self.token)
        return self.response

    def payment_charge_3d(self, payment_charge: dict):
        """

        POST /api/v2/payments/initiates

        :param dict payment_charge:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_payment_charge_3d(schema=payment_charge)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, payment_charge, self.token)
        return self.response

    def tokenize(self, payment_charge: dict):
        """

        POST /api/v2/payments/tokenize

        :param dict payment_charge:
            A non optional dict, the payload

        :returns Any self.response

        """
        self.requires_token = True
        CardValidator.is_valid_tokenize(schema=payment_charge)
        self.response = self.post_request(IClientConstants.TOKENIZATION_ENDPOINT, payment_charge, self.token)
        return self.response
