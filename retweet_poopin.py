import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'wxjQaFdC5iCsFjq4RzeqL1H5e'
consumer_secret = '3Pw8uFcPmhPjFCcmKhsNHFa6qk56GPW1ClkhCy48Xa9joLABem'
access_token = '2633116405-evYnmdrgC4P1jeUlHNkoitWLzf3hjsEacVT9p6l'
access_token_secret = 'VHfXcKbop4hedjqKBwSMIizDR4pkN5uh0cHxPzjt3YQwZ'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
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

    print "Showing all new tweets for #poopin:"
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['#poopin'])