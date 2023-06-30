import tweepy
from datetime import datetime
import time
import os

# Twitter API credentials
api_key = os.environ.get("api_key")
api_secret= os.environ.get("api_secret")
bearer_token= os.environ.get("bearer_token")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def tweet(text,period=3,tours=1,timestamp=False):
    i=0
    h=text
    while i<tours:
        if timestamp==True:    
            client.create_tweet(text=f"{h}:: {i} {datetime.now().timestamp()}")
        else:
            client.create_tweet(text=f"{h}:: {i}")
        i+=1
        
        time.sleep(period)

def reply_to_tweet(id,text):
    client.create_tweet(in_reply_to_tweet_id=id,text=text)


#tweet('tweeet No ',period=3,tours=2)
#reply_to_tweet('1576633661038145537','This is an ad for our product WINDSCRIBE VPN')