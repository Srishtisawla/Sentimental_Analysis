from textblob import TextBlob
import tweepy
import numpy as np

consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #enter your values
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #enter your values

access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #enter your values
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' #enter your values

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets1 = api.search('#Sridevi')
public_tweets2 = api.search('#PNB')
polarity1 = []
polarity2 = []
for tweet1 in public_tweets1:
    #print tweet1.text
    analysis1 = TextBlob(tweet1.text)
    polarity1.append(analysis1.sentiment[0])
polarity1 = np.array(polarity1)
mean1 = np.mean(polarity1)
print mean1

for tweet2 in public_tweets2:
    #print tweet2.text
    analysis2 = TextBlob(tweet2.text)
    polarity2.append(analysis2.sentiment[0])
polarity2 = np.array(polarity2)
mean2 = np.mean(polarity2)
print mean2
