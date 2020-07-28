"""Draft of our Slack Chatbot.

# Diary

7/27 - This Watson linked Chatbot looks like exactly what we need.
https://api.slack.com/tutorials/watson-sentiment
Maybe this too for learning about webhooks.  This seems like an easier solution.
https://blog.bearer.sh/consume-webhooks-with-python/

7/27 - Basic auth is in place and we can chat to a channel.  Need to figure out the
Events api so we can get notified.  I've updated secrets.

7/27 - We rebuit the app and added scopes.  They gave us a fun bot user token
and we put it in secrets.

7/27 - We're hung up Oath2 vs. old tokens which is the legacy system.  We're going to
backup and start from scratch because they've got a legacy systm that we're mixed up
with.  Working from here: https://api.slack.com/authentication/basics



"""
# Imports
################################################################################
import json
import requests
import re
import toml

# Constants
################################################################################
cnf = toml.load('secrets.toml')
token = cnf['SlackSecrets']['BotOathToken']

channel = 'CUCGQMTHN'
message = 'I\'m alive! Hello world.'

# Functions
################################################################################

def print_channels(f_token):
    files = {
             'token': (None, f_token),
            }

    response = requests.post('https://slack.com/api/conversations.list', files=files)
    parsed_resp = json.loads(response.content)

    for channel in parsed_resp['channels']:
        print(channel['id'], " ", channel['name'])

    # print(json.dumps(parsed_resp, indent=4, sort_keys=True))

    return True


def post_to_channel(f_token, f_channel, f_message):
    files = {
        'token': (None, f_token),
        'channel': (None, f_channel),
        'text': (None, f_message),
    }

    response = requests.post('https://slack.com/api/chat.postMessage', files=files)

    print(response)
    print(response.content)

    return True


# Run Script
################################################################################

print_channels(token)

# post_to_channel(token, channel, message)

print('End Of File')
