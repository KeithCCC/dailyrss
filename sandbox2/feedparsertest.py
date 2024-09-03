import requests
from bs4 import BeautifulSoup
from rdflib import Graph
import feedparser

def extract_urls_title(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rss_urls = []
    for link in soup.find_all('link', type='application/rss+xml'):
        rss_urls.append([link.get('title'), link.get('href')])

    return rss_urls

# l = extract_urls_title("https://win-tab.net/")
# feeds = []
# for url in l:
#     feed = feedparser.parse(url[1])
#     feeds.append(feed)
# for feed in feeds:
#     print("base url:"+feed.feed.link)
#     for entry in feed.entries:
#         print("each link:"+entry.link)
#         if 'published' in entry:
#             print(entry.published)
#         print(entry.title)
#         print(entry.link)
#         print('---------------------------------')
l = extract_urls_title("https://win-tab.net/")
feeds = []
with open('rss.txt','w') as f:
    for url in l:
        feed = feedparser.parse(url[1])
        feeds.append(feed)
    for feed in feeds:
        print("base url:"+feed.feed.link)
        for entry in feed.entries:
            print("each link:"+entry.link, end="\n\n", file=f)
            if 'published' in entry:
                print("published:"+ entry.published, end="\n\n", file=f)
            print("title:" + entry.title, end="\n\n", file=f)
            print("link:" + entry.link, end="\n\n", file=f)
            print('---------------------------------', end="\n\n", file=f)