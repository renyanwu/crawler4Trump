import tweepy
 
consumer_key = '76xWHfx9daJckY6VTzrOSaC5d'
consumer_secret = 'irLoKyPrGRC71KFQlFphDezVGOAG410UlteIGMP9sVc1tF8I45'
access_token = '1039739675949318147-PzHBrE3RWbAJpWBLPGGsvXi4f7Dv4I'
access_token_secret = 'Pk6YlilJiHWVFepnLKaeDJipJHpcVjaBUeLqiuGnZIFOQ'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)
 
DT_tweets = api.user_timeline('realDonaldTrump')

tweets = []
for tweet in DT_tweets:
	tweets.append({'time':tweet.created_at, 'text':tweet.text})
	
print(tweets)
	