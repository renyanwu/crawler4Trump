# crawler4Trump

For CNN part

At first, I planned to use the python crawler to crawl directly from  https://www.cnn.com/search/?q=trump&size=25 to get links to the articles. However, because of the anti-crawler mechanism of the website, it becomes very complicated and I should use selenium if I go this way. I don't do that because it is not easy to show the results and the response time will be long.

I found there are two special pages of CNN showing the information about Trump (https://www.cnn.com/specials/politics/president-donald-trump-45 and https://www.cnn.com/specials/politics/trump-white-house) and there is no anti-crawler. But the disadvantage is the amound of the news cannot be guaranteed to be 25 all the time. The amount is unstable at different times.


For Twitter part

Use the tweepy API  to crawl the tweets, but there are only 20 tweets can be obtained.



