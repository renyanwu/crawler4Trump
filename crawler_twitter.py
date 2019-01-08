import tweepy
 
consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx-xxxx'
access_token_secret = 'xxxx'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
 
DT_tweets = api.user_timeline('realDonaldTrump')

tweets = []
for tweet in DT_tweets:
	tweets.append({'time':tweet.created_at, 'text':tweet.text})
	
print(tweets)
	
