"""This is the draft of the twitter chatbot.  We're current (7/26) switching to
Slack for our first bot.

"""

from twython import Twython
import bot_secrets.twit_secrets as secret
from time import sleep
import rover_tempsensor as sensor

# tweets['statuses'][0]
# tweettext = tweets['statuses'][0]['text']
# uname = "@" + tweets['statuses'][0]['user']['screen_name']
#
# tweetStr = uname + ' ' + tweetStr


#Twitter Funcs
#############################################
def get_latest_tweet():
    tweets = twitter.search(q=SearchTerm, result_type='latest')
    return tweets['statuses'][0]


# Initialize
#############################################
def ChatInitialize():

    global SearchTerm, twitter

    SearchTerm = '%40nasabackyard'

    twitter = Twython(secret.apiKey, secret.apiSecret, secret.accessToken, secret.accessTokenSecret)


# Chat loop
#############################################
def ChatLoop():

    print('Checking for new tweets...')

    ChatExit = False

    PreviousTweetTime = get_latest_tweet()['id']

    while ChatExit == False:

        print('Checking for new tweets...')

        CurrentTweet = get_latest_tweet()
        CurrentTemp = "%.2f degrees" % (sensor.get_temp()*1.8 + 32)
        print(CurrentTemp)

        if CurrentTweet['id'] > PreviousTweetTime:
            UName = "@" + CurrentTweet['user']['screen_name']
            TweetText = CurrentTweet['text']
            if TweetText == '*what*temp*':
                RespString = 'My Temp is {0}'.format(CurrentTemp)
                ResponseTweet = UName + ' ' + RespString
                twitter.update_status(status=ResponseTweet)
            else:
                RespString = 'I can hear you, I just don\'t know what to say.'
                ResponseTweet = ResponseTweet = UName + ' ' + RespString
                twitter.update_status(status=ResponseTweet)

        # Exit the if statement and sleep
        sleep(120)

    return True


# Execute
#############################################

ChatInitialize()

ChatLoop()
