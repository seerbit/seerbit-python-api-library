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
    def is_valid_authorize(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "accountName" not in schema:
            msg += "\"accountName\" field is required\n"
        if "bankCode" not in schema:
            msg += "\"bankCode\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if "paymentType" not in schema:
            msg += "\"paymentType\" field is required\n"
        if msg != "\"paymentType\" field is required\n":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_validate(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "otp" not in schema:
            msg += "\"otp\" field is required\n"
        if "linkingReference" not in schema:
            msg += "\"linkingReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class CardValidator(object):

    @staticmethod
    def is_valid_authorize(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in schema:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "fullName" not in schema:
            msg += "\"fullName\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_validate(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "transaction" not in schema:
            msg += "\"transaction\" field is required\n"
        elif schema["transaction"]:
            schema = schema["transaction"]
            if "otp" not in schema:
                msg += "\"otp\" field is required\n"
            if "linkingreference" not in schema:
                msg += "\"linkingreference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_preauth(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in schema:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_capture(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "productDescription" not in schema:
            msg += "\"productDescription\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_refund(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_cancel(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_charge_non3d(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in schema:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_charge_3ds(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in schema:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "fullName" not in schema:
            msg += "\"fullName\" field is required\n"
        if "paymentType" not in schema:
            msg += "\"paymentType\" field is required\n"
        if "channelType" not in schema:
            msg += "\"channelType\" field is required\n"
        if "retry" not in schema:
            msg += "\"retry\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_payment_charge_3d(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "cvv" not in schema:
            msg += "\"cvv\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "fullName" not in schema:
            msg += "\"fullName\" field is required\n"
        if "paymentType" not in schema:
            msg += "\"paymentType\" field is required\n"
        if "channelType" not in schema:
            msg += "\"channelType\" field is required\n"
        if "retry" not in schema:
            msg += "\"retry\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_tokenize(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class MobileMoneyValidator(object):

    @staticmethod
    def is_valid_authorize(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "mobileNumber" not in schema:
            msg += "\"mobileNumber\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "paymentType" not in schema:
            msg += "\"paymentType\" field is required\n"
        if "network" not in schema:
            msg += "\"network\" field is required\n"
        if schema["network"]:
            if schema["network"] not in ["AIRTEL", "TIG", "VODAFONE", "MTN"]:
                msg += "enter a valid network provider\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class OrderValidator(object):

    @staticmethod
    def is_valid_authorize(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if "orderType" not in schema:
            msg += "\"orderType\" field is required\n"
        if "orders" in schema:
            for orders in schema["orders"]:
                if "orderId" not in orders:
                    msg += "\"orderId\" field in \"orders\" element is required\n"
                    break
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class RecurringValidator(object):

    @staticmethod
    def is_valid_create_subscription(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "cardNumber" not in schema:
            msg += "\"cardNumber\" field is required\n"
        if "expiryMonth" not in schema:
            msg += "\"expiryMonth\" field is required\n"
        if "callbackUrl" not in schema:
            msg += "\"callbackUrl\" field is required\n"
        if "expiryYear" not in schema:
            msg += "\"expiryYear\" field is required\n"
        if "cvv" not in schema:
            msg += "\"cvv\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "startDate" not in schema:
            msg += "\"startDate\" field is required\n"
        if "billingCycle" not in schema:
            msg += "\"billingCycle\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if "billingPeriod" not in schema:
            msg += "\"billingPeriod\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_update_subscription(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "mobileNumber" not in schema:
            msg += "\"mobileNumber\" field is required\n"
        if "status" not in schema:
            msg += "\"status\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid

    @staticmethod
    def is_valid_recurring_debit(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "authorizationCode" not in schema:
            msg += "\"authorizationCode\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid


class StandardCheckoutValidator(object):

    @staticmethod
    def is_valid_checkout(schema: dict) -> bool:
        msg = ""
        is_valid = True
        if "publicKey" not in schema:
            msg += "\"publicKey\" field is required\n"
        if "paymentReference" not in schema:
            msg += "\"paymentReference\" field is required\n"
        if "callbackUrl" not in schema:
            msg += "\"callbackUrl\" field is required\n"
        if "amount" not in schema:
            msg += "\"amount\" field is required\n"
        if "currency" not in schema:
            msg += "\"currency\" field is required\n"
        if "country" not in schema:
            msg += "\"country\" field is required\n"
        if "email" not in schema:
            msg += "\"email\" field is required\n"
        if "productId" not in schema:
            msg += "\"productId\" field is required\n"
        if "productDescription" not in schema:
            msg += "\"productDescription\" field is required\n"
        if msg != "":
            is_valid = False
        if not is_valid:
            raise ValueError(msg)
        return is_valid
