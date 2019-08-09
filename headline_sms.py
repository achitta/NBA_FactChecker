# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message
from nba_stats import nba_data
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    # """Respond to incoming messages with a friendly SMS."""
    player = request.values.get('Body', None)
    print(player)   
    nba_obj = nba_data()
    nba_obj.printHeadlineStats(full_name=player)
    score_file = open('headline_stats.txt','r')
    headline = score_file.read()
    print(headline)
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(headline)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
