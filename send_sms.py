# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC829a81f6a45c469f693b885fd98063e4'
auth_token = '83d0d00384d8da81e3d44c4fe1a53015'
client = Client(account_sid, auth_token)

score_file = open('scores.txt','r')
string = score_file.read()
print(string)

message = client.messages \
                .create(
                     body=string,
                     from_='+12489343292',
                     to='+12489204557'
                 )

print(message.sid)