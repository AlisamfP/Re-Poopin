import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'md9JnOCukpn2r2p46wRp1IcfH'
consumer_secret = 'Qw9OE2GddvjnALDU9XwIcOMK6Qo1x32zTlUfRuxjW5KI3DIKcU'
access_token = '115287081-FPXnA1fnjDGHGGIV3dRmUkhdl3xZFfLtTNQvgcpH'
access_token_secret = '9hbsWS0PLPz0LASoVFIXiWER1wMeAaETx07c7QQY3PH4s'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #poopin:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#poopin'])