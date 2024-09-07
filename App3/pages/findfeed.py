from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json

def find_rss_xml(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        rss_links = soup.find_all('link', type='application/rss+xml')
        
        results = []
        for link in rss_links:
            href = link.get('href')
            title = link.get('title', 'No Title')
            results.append({'href': href, 'title': title})
        
        return results
    except requests.exceptions.RequestException as e:
        return []  # Return an empty list if there's an error

st.title("Find RSS XML")
url = st.text_input("URLを入力してください")

if st.button("RSSを検索"):
    rss_feeds = find_rss_xml(url)
    for i, feed in enumerate(rss_feeds):
        st.subheader(f"RSS Feed {i+1}")
        st.text(f"Title: {feed['title']}")
        st.text(f"Link: {feed['href']}")
        # st.text_area("Link", feed['href'], height=10, disabled=True, key=f"key_{i}")

