import requests

r = requests.get("https://stream.twitter.com/1.1/statuses/sample.json")

print(r.text)
