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


class AccountValidator(object):

    @staticmethod
    def is_valid_authorize(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "accountName" not in payload:
            msg += "\"accountName\" field is required\n"
        if "bankCode" not in payload:
            msg += "\"bankCode\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_validate(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "otp" not in payload:
            msg += "\"otp\" field is required\n"
        if "linkingReference" not in payload:
            msg += "\"linkingReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class CardValidator(object):

    @staticmethod
    def is_valid_authorize(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in payload:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in payload:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in payload:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in payload:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "fullName" not in payload:
            msg += "\"fullName\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_validate(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "otp" not in payload:
            msg += "\"otp\" field is required\n"
        if "linkingReference" not in payload:
            msg += "\"linkingReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_preauth(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if "cardNumber" not in payload:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in payload:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in payload:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in payload:
            msg += "\"expiryYear\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_capture(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "productDescription" not in payload:
            msg += "\"productDescription\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_refund(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_cancel(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_charge_non3d(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in payload:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in payload:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in payload:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in payload:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_charge_3ds(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in payload:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in payload:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in payload:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in payload:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "fullName" not in payload:
            msg += "\"fullName\" field is required\n"
        if "paymentType" not in payload:
            msg += "\"paymentType\" field is required\n"
        if "channelType" not in payload:
            msg += "\"channelType\" field is required\n"
        if "retry" not in payload:
            msg += "\"retry\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_charge_3d(payload: dict) -> bool:
        return True


class MobileMoneyValidator(object):

    @staticmethod
    def is_valid_authorize(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "mobileNumber" not in payload:
            msg += "\"mobileNumber\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "paymentType" not in payload:
            msg += "\"paymentType\" field is required\n"
        if "network" not in payload:
            msg += "\"network\" field is required\n"
        if payload["network"]:
            if payload["network"] not in ["AIRTEL", "TIG", "VODAFONE", "MTN"]:
                msg += "enter a valid network provider\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class OrderValidator(object):

    @staticmethod
    def is_valid_authorize(payload: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if "orderId" not in payload:
            msg += "\"orderId\" field is required\n"
        if "orderType" not in payload:
            msg += "\"orderType\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class RecurringValidator(object):

    @staticmethod
    def is_valid_create_subscription(self, payload) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "cardNumber" not in payload:
            msg += "\"cardNumber\" field is required\n"
        if "expiryMonth" not in payload:
            msg += "\"expiryMonth\" field is required\n"
        if "callbackUrl" not in payload:
            msg += "\"callbackUrl\" field is required\n"
        if "expiryYear" not in payload:
            msg += "\"expiryYear\" field is required\n"
        if "cvv" not in payload:
            msg += "\"cvv\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "startDate" not in payload:
            msg += "\"startDate\" field is required\n"
        if "billingCycle" not in payload:
            msg += "\"billingCycle\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if "customerId" not in payload:
            msg += "\"customerId\" field is required\n"
        if "billingPeriod" not in payload:
            msg += "\"billingPeriod\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_update_subscription(self, payload) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in payload:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "country" not in payload:
            msg += "\"country\" field is required\n"
        if "mobileNumber" not in payload:
            msg += "\"mobileNumber\" field is required\n"
        if "status" not in payload:
            msg += "\"status\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_recurring_debit(self, payload) -> bool:
        msg = ""
        is_valid = True
        if "authorizationCode" not in payload:
            msg += "\"authorizationCode\" field is required\n"
        if "amount" not in payload:
            msg += "\"amount\" field is required\n"
        if "currency" not in payload:
            msg += "\"currency\" field is required\n"
        if "paymentReference" not in payload:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in payload:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid
