
<div align="center">
 <img width="200" valign="top" src="https://res.cloudinary.com/dy2dagugp/image/upload/v1571249658/seerbit-logo_mdinom.png">
</div>


<h1 align="center">
  seerbit-python-v2
</h1>

<h4 align="center">
  A Seerbit API Library for Python (Version 2)
</h4>

## Features

The Library supports all APIs under the following services:
* Payments via API (mobile money, cards, account, etc.)
* Recurring Payments
* Transaction Status

## Getting Started

A full getting started guide for integrating SeerBit can be found at [getting started docs](https://doc.seerbit.com).

## Documentation

The documentation, installation guide, detailed description of the SeerBit API and all of its features is [available on the documentation website](https://doc.seerbit.com/api/library)


## Requirements

* Python 3.7 
* Pip


## Installation

### Pip

Run this command on the terminal:

```code
pip install seerbit-python-v2
```

## Contributing

You can contribute to this repository so that anyone can benefit from it:

* Improved features
* Resolved bug fixes and issues

## Examples  

You can also check the [demos](https://github.com/seerbit/seerbit-python-api-library/tree/master/demos)
## Using the Library

<strong><h4>Initiate Account Option</h4></strong>
Instantiate a client and set the parameters. 

```python
    from seerbit.client import Client
    from seerbit.enums import EnvironmentEnum
    from seerbit.seerbitlib import Seerbit
    
    client = Client()
    client.api_base = Seerbit.LIVE_API_BASE
    client.environment = EnvironmentEnum.LIVE.value
    client.private_key = "private_key"
    client.public_key = "public_key"
    client.timeout = 20
```

To initiate a transaction request you need to perform authentication operation and acquire a token. 

```python
    from seerbit.service.authentication import Authentication

    auth_service = Authentication(client)
    auth_service.auth()
    token = auth_service.get_token()
```

After you have retrieved your token, pass it to the AccountService constructor along with your client object. You can then construct your payload and call the <code>authorize()</code> method of the AccountService class.
```python
    from random import randint
    from seerbit.service.account_service import AccountService
    
    random_number = randint(10000000, 99999999)
    payment_ref = "SBT_" + str(random_number)
    account_payload = {
        "publicKey": client.public_key,
        "amount": "100.00",
        "fee": "10",
        "fullName": "John Doe",
        "mobileNumber": "08037456590",
        "currency": "NGN",
        "country": "NG",
        "paymentReference": payment_ref,
        "email": "johndoe@gmail.com",
        "productId": "Foods",
        "productDescription": "Uba Account Transaction ",
        "clientAppCode": "kpp64",
        "channelType": "BANK_ACCOUNT",
        "redirectUrl": "https://checkout.seerbit.com",
        "deviceType": "Apple Laptop",
        "sourceIP": "127.0.0.1:3456",
        "accountName": "John S Doe",
        "accountNumber": "1234567890",
        "bankCode": "033",
        "bvn": "12345678901",
        "dateOfBirth": "04011984",
        "retry": "false",
        "invoiceNumber": "1234567891abc123ac"
    }
    account_service = AccountService(client, token)
    json_response = account_service.authorize(account_payload)
``` 

Find more examples [here](https://github.com/seerbit/seerbit-python-api-library/tree/master/demos).

## Licence
GNU General Public License. For more information, see the LICENSE file.

## Website
* https://seerbit.com
