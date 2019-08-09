# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message
from nba_stats import nba_data
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    # """Respond to incoming messages with a friendly SMS."""
    incoming = request.values.get('Body', None)
    print(incoming)   

    message_body = ""
    if(incoming.find(", Season")!=-1) :
        #GET SEASON STATS
        idx = incoming.find(", Season")
        player_name = incoming[0:idx]
        nba_obj = nba_data()
        nba_obj.printSeasonStats(my_name=player_name)
        season_file = open('season_stats.txt', 'r')
        season_stats = season_file.read()
        print(season_stats)
        message_body = season_stats

    else:
        # Headline stat
        nba_obj = nba_data()
        nba_obj.printHeadlineStats(full_name=incoming)
        score_file = open('headline_stats.txt','r')
        headline = score_file.read()
        print(headline)
        message_body = headline
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(message_body)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
