##################################################
# RSS reader
##################################################

#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser

def create_opml_from_urls(url_list, output_file):
    root = ElementTree.Element("opml")
    head = ElementTree.SubElement(root, "head")
    body = ElementTree.SubElement(root, "body")

    for url in url_list:
        outline = ElementTree.SubElement(body, "outline", {"type": "rss", "xmlUrl": url})

    tree = ElementTree.ElementTree(root)
    tree.write(output_file)

#1. Read Rss data
#2. return list of rss url
#3. Register site
#4. Store in OPML
#5. Show rss contents

def extract_rss_urls(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rss_urls = []
    for link in soup.find_all('link', type='application/rss+xml'):
        rss_urls.append(link.get('href'))

    return rss_urls

def ShowFeed():
    if "source_site" not in st.session_state:
        st.session_state["source_site"] = ""
    source_site = 'empty'
    st.title("RSS Feed Extractor")
 #   source_site = read_source_site()
 #   st.text(st.session_state["source_site"])
    rss_feeds = extract_rss_urls(st.session_state["source_site"])
    
    for item in rss_feeds:
        feed = feedparser.parse(item)
        for entry in feed.entries:
            if 'published' in entry:
                st.text(entry.published)
            st.write(entry.title)
            st.text(entry.link)
            st.write(entry.summary)
            st.text('---------------------------------')
            
    

    
ShowFeed()
# if __name__ == "__main__":
