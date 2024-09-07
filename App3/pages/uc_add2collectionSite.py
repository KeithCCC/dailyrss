# input url
# test url
# search for xml, rdf
# add to collection
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json
st.title("Add to collection")

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

if 'checkbox_rss' not in st.session_state:
        st.session_state.checkbox_rss = {}

if st.button("RSSを検索"):
    rss_feeds = find_rss_xml(url)
    with st.form("my_form"):
        for i, feed in enumerate(rss_feeds):
            st.session_state.checkbox_rss[feed['href']] = st.checkbox(
            f"{feed['title']}\n{feed['href']}",
            key=f"feed_{i}"
        )
        submitted = st.form_submit_button("RSSを追加")
        if submitted:
            st.text(st.session_state.checkbox_rss)
