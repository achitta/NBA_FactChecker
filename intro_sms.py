# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'INSERT HERE'
auth_token = 'INSERT HERE'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Welcome to Aditya's NBA Updates. You will receive daily updates on NBA scores. Also, you can receive career stats of your favorite player by typing their full name (Ex. 'Stephen Curry')",
                     from_='+12489343292',
                     to='+12489204557'
                 )

print(message.sid)
