from twitter import *

twitter_stream = TwitterStream(
    auth = OAuth(
consumer_key = '[md9JnOCukpn2r2p46wRp1IcfH]',
consumer_secret = '[Qw9OE2GddvjnALDU9XwIcOMK6Qo1x32zTlUfRuxjW5KI3DIKcU]',
access_token = '[115287081-FPXnA1fnjDGHGGIV3dRmUkhdl3xZFfLtTNQvgcpH]',
token_secret = '[9hbsWS0PLPz0LASoVFIXiWER1wMeAaETx07c7QQY3PH4s]'
))

iterator = twitter_stream.statuses.filter('#poopin')


for tweet in iterator:
    print msg['text']
