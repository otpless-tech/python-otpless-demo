# Merchant Integration Documentation(Backend Python Auth SDK)

---

> ## A. OTPLessAuth Dependency
>
> install Below dependency in your project's

```shell
pip install OTPLessAuthSDK
```

you can also get latest version of dependency
at https://pypi.org/project/OTPLessAuthSDK

---

> ## B. OTPLessAuth class

The `OTPLessAuth` class provides methods to integrate OTPLess authentication into your Python backend application. This
documentation explains the usage of the class and its methods.

### Methods:

---

> ### 1. decodeIdToken

---

This method help to resolve `idToken(JWT token)` which is issued by `OTPLess` which return user detail
from that token also this method verify that token is valid, token should not expired and
issued by only `otpless.com`

##### Method Signature:

```python
decode_id_token(id_token, client_id, client_secret, audience=None)
```

#### Method Params:

| Params       | Data type | Mandatory | Constraints | Remarks                                                                      |
| ------------ | --------- | --------- | ----------- | ---------------------------------------------------------------------------- |
| idToken      | String    | true      |             | idToken which is JWT token which you get from `OTPLess` by exchange code API |
| clientId     | String    | true      |             | Your OTPLess `Client Id`                                                     |
| clientSecret | String    | true      |             | Your OTPLess `Client Secret`                                                 |

#### Return

Return:
Object Name: UserDetail

```json
{'success': True, 'auth_time': 1697649943, 'phone_number': '+9193******', 'email': 'dev***@gmail.com', 'name': 'Devloper From OTP-less', 'country_code': '+91', 'national_phone_number': '9313******'}
```

> ### 2. verify code

---

This method help to resolve `code` which is return from `OTPLess` which will return user detail
from that code also this method verify that code is valid, code should not expired and
issued by only `otpless.com`

##### Method Signature:

```python
verify_code(code, client_id, client_secret, audience)
```

#### Method Params:

| Params       | Data type | Mandatory | Constraints | Remarks                           |
| ------------ | --------- | --------- | ----------- | --------------------------------- |
| code         | String    | true      |             | code which you get from `OTPLess` |
| clientId     | String    | true      |             | Your OTPLess `Client Id`          |
| clientSecret | String    | true      |             | Your OTPLess `Client Secret`      |

#### Return

Return:
Object Name: UserDetail

```json
{'success': True, 'auth_time': 1697649943, 'phone_number': '+9193******', 'email': 'dev***@gmail.com', 'name': 'Devloper From OTP-less', 'country_code': '+91', 'national_phone_number': '9313******'}
```

> ### 3. Verify Auth Token

---

This method help to resolve `token` which is issued by `OTPLess` which return user detail
from that token also this method verify that token is valid, token should not expired and
issued by only `otpless.com`

##### Method Signature:

```python
verify_token(token, client_id, client_secret)
```

#### Method Params:

| Params       | Data type | Mandatory | Constraints | Remarks                            |
| ------------ | --------- | --------- | ----------- | ---------------------------------- |
| token        | String    | true      |             | token which you get from `OTPLess` |
| clientId     | String    | true      |             | Your OTPLess `Client Id`           |
| clientSecret | String    | true      |             | Your OTPLess `Client Secret`       |

#### Return

Return:
Object Name: UserDetail

```json
{'success': True, 'auth_time': 1697649943, 'phone_number': '+9193******', 'email': 'dev***@gmail.com', 'name': 'Devloper From OTP-less', 'country_code': '+91', 'national_phone_number': '9313******'}
```

> ### 4. Generate Magic link

---

The Authorization Endpoint initiates the authentication process by sending a `magic link` to the user's WhatsApp or email, based on the provided contact information. This link is used to verify the identity of the user. Upon the user's action on this link, they are redirected to the specified URI with an authorization code included in the redirection.

##### Method Signature:

```python
generate_magic_link(mobile_number, email, client_id, client_secret,redirect_uri,channel)
```

#### Method Params:

| Params        | Data type | Mandatory | Constraints                                       | Remarks                                                                                               |
| ------------- | --------- | --------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| channel       | String    | false     | if no channel given WHATSAPP is chosen as default | WHATSAPP/SMS                                                                                          |
| mobile_number | String    | false     | At least one required                             | The user's mobile number for authentication in the format: country code + number (e.g., 91XXXXXXXXXX) |
| email         | String    | false     | At least one required                             | The user's email address for authentication.                                                          |
| redirect_uri  | String    | true      |                                                   | The URL to which the user will be redirected after authentication. This should be URL-encoded         |
| clientId      | String    | true      |                                                   | Your OTPLess `Client Id`                                                                              |
| clientSecret  | String    | true      |                                                   | Your OTPLess `Client Secret`                                                                          |

#### Return

Return:
Object Name: RquestIds

```json
{'mobile_request_id': '72bf8ccdb56949c18fa141452c3b42a6', 'email_request_id': 'e3600742ff6049de85d0fe60995beefe', 'success': True}
```

Mobile

```json
{'mobile_request_id': 'a624bb06e0c0433a92a095e06f80a995', 'destination_uri': 'https://wa.me/911141169439', 'success': True}
```

---

> ## C. OTP class

These methods enable you to send, resend and verify OTP.

### Methods:

---

> ### 1. Send OTP

---

##### Method Signature:

```python
send_otp(phoneNumber, email, channel,hash, orderId, expiry, otpLength,client_id,client_secret)
```

#### Method Params:

| Params       | Data type | Mandatory | Constraints                                                     | Remarks                                                           |
| ------------ | --------- | --------- | --------------------------------------------------------------- | ----------------------------------------------------------------- |
| phoneNumber  | String    | true      |                                                                 | Mobile Number of your users                                       |
| email        | String    | true      |                                                                 | Mail Id of your users                                             |
| orderId      | String    | false     |                                                                 | An Merchant unique id for the request.                            |
| expiry       | Int       | false     |                                                                 | OTP expiry in sec                                                 |
| hash         | String    | false     |                                                                 | An Hash will be used to auto read OTP.                            |
| clientId     | String    | true      |                                                                 | Your OTPLess `Client Id`                                          |
| clientSecret | String    | true      |                                                                 | Your OTPLess `Client Secret`                                      |
| otpLength    | Integer   | false     | 4 or 6 only allowed                                             | Allowes you to send OTP in 4/6 digit. default will be 6 digit.    |
| channel      | String    | false     | SMS/WHATSAPP/ALL (if no channel given SMS is chosen as default) | Allowes you to send OTP on WhatsApp/SMS/Both. default will be SMS |

#### Return

Return:
Object Name: OTPResponse

```json
{
  "orderId": "Otp_ED5F709E1C6B41EB8C0595C7968354EB"
}
```

### 2. Resend OTP

##### Method Signature:

```python
    resend_otp(orderId, client_id, client_secret)
```

#### Method Params:

| Params       | Data type | Mandatory | Constraints | Remarks                                |
| ------------ | --------- | --------- | ----------- | -------------------------------------- |
| orderId      | String    | true      |             | An Merchant unique id for the request. |
| clientId     | String    | true      |             | Your OTPLess `Client Id`               |
| clientSecret | String    | true      |             | Your OTPLess `Client Secret`           |

#### Return

Return:
Object Name: OTPResponse

```json
{
  "orderId": "DP0000111"
}
```

---

### 3. Verify OTP

##### Method Signature:

```python
    veriy_otp(orderId, otp, email, phoneNumber, client_id, client_secret)
```

#### Method Params:

| Params       | Data type | Mandatory | Constraints | Remarks                                     |
| ------------ | --------- | --------- | ----------- | ------------------------------------------- |
| email        | String    | true      |             | An email on which OTP has been sent.        |
| phoneNumber  | String    | true      |             | An phone number on which OTP has been sent. |
| orderId      | String    | true      |             | An Merchant unique id for the request.      |
| otp          | String    | true      |             | OTP value.                                  |
| clientId     | String    | true      |             | Your OTPLess `Client Id`                    |
| clientSecret | String    | true      |             | Your OTPLess `Client Secret`                |

#### Return

Return:
Object Name: OTPVerificationResponse

- `reason` (String): The will be errorMessage in case of OTP doesn't verified

```json
{
  "isOTPVerified": true
}
```

---

> ### UserDetail Object Fields:
>
> `success` (boolean): This will be `true` in case of method successfully performed operation.<br> > `authTime` (Long, required): The time when authentication was completed.<br> > `phoneNumber` (String, required): The user's phone number.<br> > `countryCode` (String, required): The country code of user's phone number.<br> > `nationalPhoneNumber` (String, required): The user's phone number without country code.<br> > `email` (String, required): The user's email address.<br> > `name` (String, required): The user's full name.<br>

### Error case:

`success` (boolean): This will be `false`. The method is failed to perform.<br>
`errorMessage` (String): The message contains error information.<br>

### Example of usage

```python
import OTPLessAuthSdk

# Setup necessary parameters
client_id = "your_client_id"
client_secret = "your_client_secret"
code = "your_id_token_here"
audience = None

# Use the verify_code function to verify the code and get user details
try:
    user_details = OTPLessAuthSDK.UserDetail.verify_code(code, client_id, client_secret, audience)


    print(user_details.success)
    print(user_details.auth_time)
    print(user_details.phone_number)
    print(user_details.email)
    print(user_details.name)
    print(user_details.country_code)
    print(user_details.national_phone_number)


    print(f"User details: {user_details}")
except Exception as e:
    print(f"An error occurred: {e}")
```

This method allows you to decode and verify OTPLess ID tokens and retrieve user information for integration into your
backend Python application.
