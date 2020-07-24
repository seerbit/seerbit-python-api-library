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
from interface.app_interface import IClientConstants
from interface.service_interface import ICardService
from service.service import Service
from validation import CardValidator
from utility import Utility


class CardService(Service, ICardService, IClientConstants):

    def __init__(self, client, token):
        super(CardService, self).__init__(client)
        self.token = token
        Utility.non_null(client)

    def authorize(self, card: dict):
        """ POST /api/v2/payments/initiates """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_authorize(payload=card)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, card, self.token)
        return self.response

    def validate(self, transaction: dict):
        """ POST /api/v2/payments/initiates """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_validate(payload=transaction)
        self.response = self.post_request(IClientConstants.VALIDATE_CARD_PAYMENT_ENDPOINT, transaction, self.token)
        return self.response

    def preauth_authorization(self, card_pre_auth: dict):
        """ POST /api/v2/payments/authorise """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_preauth(payload=card_pre_auth)
        self.response = self.post_request(IClientConstants.PREAUTH_AUTHORIZE_ENDPOINT, card_pre_auth, self.token)
        return self.response

    def payment_capture(self, payment_capture: dict):
        """ POST /api/v2/payments/capture """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_payment_capture(payload=payment_capture)
        self.response = self.post_request(IClientConstants.PAYMENT_CAPTURE_ENDPOINT, payment_capture, self.token)
        return self.response

    def payment_refund(self, payment_refund: dict):
        """ POST /api/v2/payments/refund """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_payment_refund(payload=payment_refund)
        self.response = self.post_request(IClientConstants.PAYMENT_REFUND_ENDPOINT, payment_refund, self.token)
        return self.response

    def payment_cancel(self, payment_cancel: dict):
        """ POST /api/v2/payments/cancel """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_payment_cancel(payload=payment_cancel)
        self.response = self.post_request(IClientConstants.PAYMENT_CANCEL_ENDPOINT, payment_cancel, self.token)
        return self.response

    def payment_charge_non3d(self, payment_charge: dict):
        """ POST /api/v2/payments/charge """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_payment_charge_non3d(payload=payment_charge)
        self.response = self.post_request(IClientConstants.PAYMENT_CHARGE_ENDPOINT, payment_charge, self.token)
        return self.response

    def payment_charge_3ds(self, payment_charge: dict):
        """ POST /api/v2/payments/initiates """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_payment_charge_3ds(payload=payment_charge)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, payment_charge, self.token)
        return self.response

    def payment_charge_3d(self, payment_charge: dict):
        """ POST /api/v2/payments/initiates """
        super(CardService, self).requires_token = True
        CardValidator.is_valid_payment_charge_3d(payload=payment_charge)
        self.response = self.post_request(IClientConstants.INITIATE_PAYMENT_ENDPOINT, payment_charge, self.token)
        return self.response
