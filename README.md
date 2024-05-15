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
from flask import Flask
import OTPLessAuthSDK
import uuid

app = Flask(__name__)

# Setup necessary parameters
audience = None
clientId = "kp******ri"; # Replace with Your OTPLess `Client Id`
clientSecret = "4d********qx"; # Replace with Your OTPLess `Client Secret`
phoneNumber = "91*********"; # Replace with your mobile number
email = 'sa******8@gmail.com'; # Replace with your email ID
redirectURI = 'http://localhost:3000'; # Replace with your redirect url
channel = 'WHATSAPP';# you can use SMS
token = 'token'; # token received from magicLinkTokens
code = 'code'; # code received on your specified redirect URI
hash = 'hash'; # Your mobile application Hash
orderId = 'orderId'; # Unique Order id.
expiry = '5'; # OTP expiry in sec
otpLength = '4'; # Values like 6 or 4
otp = '4'; # Enter OTP here

@app.route('/sendMagicLink')
def sendMagicLink():
    try:
        user_details = OTPLessAuthSDK.UserDetail.generate_magic_link(phoneNumber, email, clientId, clientSecret, redirectURI, channel, audience)
        print(f"User details: {user_details}")
        return user_details
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/verifyCode')
def verifyCode():
    try:
        user_details = OTPLessAuthSDK.UserDetail.verify_code(code, clientId, clientSecret, audience)
        print(f"User details: {user_details}")
        return user_details
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/verifyToken')
def verifyToken():
    try:
        user_details = OTPLessAuthSDK.UserDetail.verify_token(token, clientId, clientSecret, audience)
        print(f"User details: {user_details}")
        return user_details
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/sendOTP')
def sendOTP():
    try:
        otp_details = OTPLessAuthSDK.OTP.send_otp(phoneNumber, email, channel, hash, "PYTHON"+str(uuid.uuid4()), expiry, otpLength, clientId, clientSecret)
        print(f"User details: {otp_details}")
        return otp_details
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/reSendOTP')
def reSendOTP():
    try:
        otp_details = OTPLessAuthSDK.OTP.resend_otp(orderId, clientId, clientSecret)
        print(f"User details: {otp_details}")
        return otp_details
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/verifyOTP')
def verifyOTP():
    try:
        otp_details = OTPLessAuthSDK.OTP.veriy_otp(orderId, otp, email, phoneNumber, clientId, clientSecret)
        print(f"User details: {otp_details}")
        return otp_details
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
```

This method allows you to decode and verify OTPLess ID tokens and retrieve user information for integration into your
backend Python application.
