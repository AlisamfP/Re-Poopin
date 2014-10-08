import tweepy
import json
import os
from flask import Flask

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = os.environ['CONS_KEY']
consumer_secret = os.environ['CONS_SEC']
access_token = os.environ['ACC_TOKEN']
access_token_secret = os.environ['TOKEN_SEC']

app = Flask(__name__)
@app.route('/')
# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        if (decoded['user']['screen_name'] != 'hashtagpoopin'):
            api = tweepy.API(auth)
            api.retweet(decoded['id'])
            return True
        else:
            return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Twitter Stream Listening for #poopin..."
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#poopin'])
