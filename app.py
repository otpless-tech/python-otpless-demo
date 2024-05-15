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