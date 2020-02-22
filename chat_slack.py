import json
import requests


# https://slack.com/api/chat.postMessage?token=xoxb-918177779717-951780844322-EAGc8kwQU7IZLbKte6sWnoJg&channel=matilda-talk&text=Hello%20World.&pretty=1

################# Post using Webhook
# headers = { 'Content-type': 'application/json', }
# data = '{"text":"Hello, World!"}'
# response = requests.post('https://hooks.slack.com/services/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', headers=headers, data=data)
# print(response.Content)


################ Post using chat api
# headers = {
#     'Authorization': 'Bearer xoxb-1234-56789abcdefghijklmnop',
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
#     'Authorization': 'Bearer xoxb-918177779717-951780844322-EAGc8kwQU7IZLbKte6sWnoJg'
# }
#
# data = """{
#     "channel":"#matilda-talk",
#     "text":"Yeah, I can talk now."}
#     """
#
# response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, data=data)
#
# print(response.content)fdgdf


headers = {
    'Content-type': 'application/x-www-form-urlencoded'
}

response = requests.get('https://slack.com/api/conversations.history?token=xoxb-918177779717-951780844322-EAGc8kwQU7IZLbKte6sWnoJg&channel=CUCGQMTHN&limit=15', headers=headers)
response = json.loads(response.content)
response = response['messages']

for message in response:
    print(message['text'])
