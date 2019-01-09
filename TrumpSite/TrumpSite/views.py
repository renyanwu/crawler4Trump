from django.shortcuts import render
import json
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import tweepy


def getpaths(paths, url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'uft-8'
    soup = BeautifulSoup(resp.text, 'html.parser')

    articles = soup.find_all("article", class_="cd")

    for i in range(len(articles) - 20, len(articles)):
        path = articles[i].find_all("a")[0].attrs['href']
        if path[1] != 'v':
            if path not in paths:
                paths.append(path)

    return paths


def getContent(path):
    url = "https://www.cnn.com" + path

    if "comhttp" in url:
        return "stop"

    print(url)
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')

    title = soup.title.string

    if len(soup.find_all("p", class_="update-time")) > 0:
        time = soup.find_all("p", class_="update-time")[0].get_text()
    else:
        time = ""

    paragraphs = soup.find_all(class_="zn-body__paragraph")
    p2str = []

    for p in paragraphs:
        p2str.append(str(p))

    print(title)
    article = {
        "title": title,
        "time": time,
        "paragraphs": p2str
    }

    return article


def index(requests):
    return render(requests, 'index.html')

def twitter(requests):
    return render(requests, 'twitter.html')

@csrf_exempt
def getArticles(requests):
    paths = getpaths([], "https://www.cnn.com/specials/politics/president-donald-trump-45")
    paths = getpaths(paths, "https://www.cnn.com/specials/politics/trump-white-house")

    articles = []

    for path in paths:
        content = getContent(path)
        if content == "stop":
            break
        articles.append(getContent(path))

    return HttpResponse(json.dumps(articles), content_type="application/json")

@csrf_exempt
def getTwitters(requests):

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
        tweets.append({'time': tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"), 'text': tweet.text})

    return HttpResponse(json.dumps(tweets), content_type="application/json")

