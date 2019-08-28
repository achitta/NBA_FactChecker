# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message
from nba_stats import nba_data
import time
from yesterday_update_sms import yesterday_scores


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():    
    if(time.localtime().tm_hour == 10 and time.localtime().tm_min == 56 and time.localtime().tm_sec == 00) :
        return

    # """Respond to incoming messages with a friendly SMS."""
    incoming = request.values.get('Body', None)
    if(incoming == "") :
        return "Hello World! No message to process at the time"
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
        nba_obj.printCareerStats(name=incoming)
        score_file = open('career_stats.txt','r')
        headline = score_file.read()
        print(headline)
        message_body = headline
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(message_body)

    return str(resp)

if __name__ == "__main__":
    if(time.localtime().tm_hour >= 2 and time.localtime().tm_hour <= 16) :
        y = yesterday_scores()
        y.yesterday_update()
    app.run(debug=True)