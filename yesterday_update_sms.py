# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from nba_stats import nba_data

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
class yesterday_scores:
    def yesterday_update(self):
        account_sid = 'INSERT'
        auth_token = 'INSERT'
        client = Client(account_sid, auth_token)

        nba_obj = nba_data()
        nba_obj.printScoresForYesterday()

        score_file = open('scores.txt','r')
        string = score_file.read()
        if(string == ""):
            string = "No games played yesterday!"
        print(string)

        message = client.messages \
                        .create(
                            body=string,
                            from_='+12489343292',
                            to='+12489204557'
                        )

        print(message.sid)