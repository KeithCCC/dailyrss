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
    
    if "sample_url" not in st.session_state:
        st.session_state["sample_url"] = ""
        sample_url = 'empty'
    
    print("show site:" + st.session_state["sample_url"])
    st.title("RSS Feed Extractor")
    
    testrul = st.text_input("Add a new site:")

    # st.text(st.session_state["sample_url"])
    
 
    #rss_feeds = extract_rss_urls(st.session_state["source"]["url"])
    btn_testlink = st.button("btn_testlink")

    rss_feeds = extract_rss_urls(testrul)
    for item in rss_feeds:
        st.write(item)

    
    # for item in rss_feeds:
    #     feed = feedparser.parse(item)
    #     for entry in feed.entries:
    #         if 'published' in entry:
    #             st.text(entry.published)
    #         st.write(entry.title)
    #         st.text(entry.link)
    #         st.write(entry.summary)
    #         st.text('---------------------------------')
            
    

    
ShowFeed()
# if __name__ == "__main__":
