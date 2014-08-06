import tweepy

auth = tweepy.OAuthHandler('md9JnOCukpn2r2p46wRp1IcfH', 'Qw9OE2GddvjnALDU9XwIcOMK6Qo1x32zTlUfRuxjW5KI3DIKcU')
auth.set_access_token('115287081-FPXnA1fnjDGHGGIV3dRmUkhdl3xZFfLtTNQvgcpH', '9hbsWS0PLPz0LASoVFIXiWER1wMeAaETx07c7QQY3PH4s')

api = tweepy.API(auth)

stream = tweepy.Stream(auth, l)
stream.filter(track=['poopin'])