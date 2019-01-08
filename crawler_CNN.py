import requests
from bs4 import BeautifulSoup
import json

def getpaths(paths, url):
    headers= {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    resp = requests.get(url, headers = headers)
    resp.encoding='uft-8'
    soup=BeautifulSoup(resp.text,'html.parser')

articles = soup.find_all("article", class_="cd")

    print(len(articles))
    for i in range(len(articles)-20, len(articles)):
        path = articles[i].find_all("a")[0].attrs['href']
        if path[1]!='v':
            if path not in paths:
                paths.append(path)

return paths

def getContent(path):
    url = "https://www.cnn.com"+path
    if "comhttp" in url:
        return "stop"
    
    print(url)
    resp = requests.get(url)
    resp.encoding='uft-8'
    soup=BeautifulSoup(resp.text,'html.parser')
    
    title = soup.title.string
    print(title)
    
    if len(soup.find_all("p", class_="update-time"))>0:
        time = soup.find_all("p", class_="update-time")[0].get_text()
        print(time)
    else:
        time = ""
    
    paragraphs = soup.find_all(class_="zn-body__paragraph")
    p2str = []
    
    for p in paragraphs:
        p2str.append(str(p))
    
    
    article = {
        "title" : title,
        "time" : time,
        "paragraphs" : p2str
    }
    
    return article



paths = getpaths([], "https://www.cnn.com/specials/politics/president-donald-trump-45")
paths = getpaths(paths, "https://www.cnn.com/specials/politics/trump-white-house")

articles = []
#getContent(paths[0])

for path in paths:
    content = getContent(path)
    if content == "stop":
        break
    articles.append(getContent(path))

print(len(articles))

with open("CNN.json","w") as f:
    json.dump(articles,f)
    print("Success...")




