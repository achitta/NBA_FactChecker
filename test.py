# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from PyQt5 import QtWidgets


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'INSERT HERE'
auth_token = 'INSERT HERE'
client = Client(account_sid, auth_token)

validation_request = client.validation_requests \
                           .create(
                                friendly_name='My Phone Number',
                                phone_number='+12343242432'
                            )

print(validation_request.friendly_name)