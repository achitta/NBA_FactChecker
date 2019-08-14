# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from PyQt5 import QtWidgets


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC829a81f6a45c469f693b885fd98063e4'
auth_token = '83d0d00384d8da81e3d44c4fe1a53015'
client = Client(account_sid, auth_token)

validation_request = client.validation_requests \
                           .create(
                                friendly_name='My Phone Number',
                                phone_number='+12489204557'
                            )

print(validation_request.friendly_name)