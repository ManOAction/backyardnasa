#!/usr/bin/env python
# import sys
from twython import Twython
import bot_secrets.twit_secrets as secret

tweetStr = "Hey! I can talk! Or at least be forced to say things like a puppet."

api = Twython(secret.apiKey, secret.apiSecret, secret.accessToken, secret.accessTokenSecret)

api.update_status(status=tweetStr)

print ("Tweeted: " + tweetStr)
