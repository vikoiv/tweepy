import tweepy
import urllib.request
import json
import random


with open('conf.json') as json_data:
    jConf = json.load(json_data)



auth = tweepy.OAuthHandler(jConf['ConsumerKey'], jConf['ConsumerKeySecret'])
auth.set_access_token(jConf['AccessToken'], jConf['AccessTokenSecret'])

api = tweepy.API(auth)



# Write a tweet to push to our Twitter account
tweet = 'Hello, world!'
api.update_status(status=tweet)

