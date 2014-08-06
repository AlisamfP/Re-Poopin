from twitter import *

auth = OAuth(
token = '[115287081-FPXnA1fnjDGHGGIV3dRmUkhdl3xZFfLtTNQvgcpH]',
token_secret = '[9hbsWS0PLPz0LASoVFIXiWER1wMeAaETx07c7QQY3PH4s]',
consumer_key = '[md9JnOCukpn2r2p46wRp1IcfH]',
consumer_secret = '[Qw9OE2GddvjnALDU9XwIcOMK6Qo1x32zTlUfRuxjW5KI3DIKcU]'
)

twitter_stream = TwitterStream(auth = auth)
iterator = twitter_stream.statuses.sample()


for tweet in iterator:
	print tweet
    # print iterator['text']
    # print iterator['user']['screen-name']
