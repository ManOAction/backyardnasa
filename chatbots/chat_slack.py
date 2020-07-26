"""Draft of our Slack Chatbot."""
import json
import requests
import re


import bot_secrets.twit_secrets as secrets






################ Post using chat api
# headers = {
#     'Authorization': 'Bearer {0}'.format(secrets.SlackToken),
#     'Content-type': 'application/json',
# }
#
# data = """{
#     "channel":"C061EG9SL",
#     "text":"Hello World, again." #,
#     # "attachments": [{"text":"Who wins the lifetime supply of chocolate?",
#     #                 "fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.",
#     #                 "color":"#3AA3E3",
#     #                 "attachment_type":"default","callback_id":"select_simple_1234",
#     #                 "actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]
#     }'
# """
# response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, data=data)


# ###############
# headers = {
#     'Content-type': 'application/x-www-form-urlencoded',
#     'Authorization': 'Bearer {0}'.format(secrets.SlackToken)
# }
#
# data = """{
#     "channel":"#matilda-talk",
#     "text":"Yeah, I can talk now."}
#     """
#
# response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, data=data)
#
# print(response.content)
# MatildaName = re.compile('<@UTZNYQU9G>')


##############################################
def get_most_recent_message():
    headers = {
        'Content-type': 'application/x-www-form-urlencoded'
        }

    MessageText = False

    response = requests.get('https://slack.com/api/conversations.history?token={0}&channel=CUCGQMTHN&limit=15'.format(secrets.SlackToken), headers=headers)
    response = json.loads(response.content)
    # print(response)
    response = response['messages']

    for message in response:
        if re.match(r"<@UTZNYQU9G>", message['text']):
            MessageText = print(message['text'])
            return MessageText

    return MessageText


def post_to_channel(message):
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer {0}'.format(secrets.SlackToken)
            }
    data = """{
        "channel":"#matilda-talk",
        "text":"{0}".}
        """.format(message)
    response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, data=data)

    return True

##############################################


while __name__ == "__main__":
