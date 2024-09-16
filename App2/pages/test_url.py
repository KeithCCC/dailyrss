#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import re

def extract_urls_title(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rss_urls = []
    for link in soup.find_all('link', type='application/rss+xml'):
        rss_urls.append([link.get('title'), link.get('href')])

    return rss_urls

def is_valid_url(url):
    # Regular expression to validate an HTML URL
    url_regex = re.compile(
        r'^(https?|ftp)://'  # http://, https://, ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    # Check if the URL matches the pattern
    return re.match(url_regex, url) is not None

def is_xml_extension(url):
    # Check if the URL ends with '.xml'
    return url.lower().endswith('.xml')

def is_xml_or_rdf(url):
    # Check if the URL ends with .xml or .rdf
    if url.lower().endswith(('.xml', '.rdf')):
        return True
def is_rdf_extension(url):
    # Check if the URL ends with '.xml'
    return url.lower().endswith('.rdf')

def sample_df():
    initial_data = [[0,"rss", "@IT", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "Atmark IT","Tech"]]
    sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description","label"])
    return sample_df 


st.title("Add new sits or rss")


if 'new_site' not in st.session_state:
    st.session_state["new_site"] = 'none'

st.text(st.session_state.df)
message = "site or rss url"

# Add a new row
st.write("Add a new site:")
new_site_url = st.text_input(message)
new_site_label = st.text_input("site label")

selected_items = {}


if st.button("Test url"):
    st.session_state.add_site = True
    rss_feeds = []
    if is_valid_url(new_site_url):
        # st.text(new_site_url)
        if is_rdf_extension(new_site_url):
            st.text("rdf")
            rss_feeds.append('URL')
        else:
            st.text("not rdf")
            rss_feeds = extract_urls_title(new_site_url)

        # for i, item in rss_feeds:
        checkbox_states = {}
        #     st.checkbox(f"{item['URL']}", key=key)
        st.text(type(rss_feeds))
        st.text(rss_feeds)
        
        # for i, item in rss_feeds:
        #     key = f"checkbox_{i}"
        #     checkbox_states[item] = st.checkbox(item[0],key=key) 
        
        for index, item in enumerate(rss_feeds):
            label = item[1]  # Assuming item is a tuple or list and the first element is the label
            checkbox_key = f"checkbox_{index}"
            checkbox_states[label] = st.checkbox(label=label, key=checkbox_key)
        
        selected_items = []
        for item in checkbox_states:
            if checkbox_states[label]:
                selected_items.append(item)
        st.write("Selected items:", selected_items)
        
        # st.text(checkbox_states)    
        
        # selected_items = [item for item in rss_feeds if checkbox_states[item]]
        # selected_items = []
        # for item in rss_feeds:
        #     if checkbox_states[item]:
        #         selected_items.append(item)
        # st.write("Selected items:", selected_items)