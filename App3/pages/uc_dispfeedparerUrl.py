from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json

st.title("Display Feedparser URL")

url = st.text_input("URLを入力してください")
feeds = feedparser.parse(url)
if st.button("RSSを表示"):
    # st.text(find_rss_xml(url))
    # st.text(feeds)
    for entry in feeds.entries:
        # st.text(entry)
        if 'published' in entry:
            st.text(entry.published)
        st.write(entry.title)
        st.write(entry.link)
        if 'summary' in entry:
            st.write(entry.summary)
        # st.write(entry.summa  ry)
        st.text(entry)
        st.text_area("Data", entry , height=100, disabled=True)

        st.text('---------------------------------')