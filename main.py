import scraping
import tweepy_setup
import tweet_cleaning
import gpt
import time

#login twitter
driver=scraping.start_login()
print('Login successful')

time.sleep(1.5)
#go to the profile where we will advertise our product
scraping.goto(driver)
print("profil page successful")

time.sleep(2)
#collect tweets
tweet_text,tweet_id=scraping.collect_tweets(driver)
print("tweet collection successful")

time.sleep(1.5)
#clean tweets
tweet_text_cleaned=[tweet_cleaning.cleaning(tweet) for tweet in tweet_text]

#generate replies
for tweet,idd in zip(tweet_text_cleaned,tweet_id):
    reply=gpt.askgpt(tweet,'Windscribe vpn')
    if reply=='Yes':
        tweepy_setup.reply_to_tweet(idd,"This is an ad for our product WINDSCRIBE VPN")
        print(f"tweet {idd} replied")