#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import re

def extract_rss_urls(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rss_urls = []
    for link in soup.find_all('link', type='application/rss+xml'):
        rss_urls.append(link.get('href'))

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

def manage_sites(df):
    st.title("Add new sits or rss")
    
    st.table(df)
    message = "site or rss url"
    
    # Add a new row
    st.write("Add a new site:")
    new_site_url = st.text_input(message)
    new_site_label = st.text_input("site label")
    
    if st.button("Add site"):
            #rss_feeds = extract_rss_urls(st.session_state["source"]["url"])
        if is_valid_url(new_site_url):
            if is_xml_or_rdf(new_site_url):
                rss_feeds = extract_rss_urls(new_site_url)
            else:
                rss_feeds.append('URL')
                
            for item in rss_feeds:
                feed = feedparser.parse(item)
                for entry in feed.entries:
                    new_row = pd.DataFrame({'Title': [entry.title],'URL': [entry.link], 'URI': [entry.link], 'Description': [entry.summary], 'Type': [new_site_label]})
                    st.session_state.news_df = pd.concat([st.session_state.news_df, new_row], ignore_index=True)
        else:
            message = "Enter site or rss url again"
                           
                       

    st.write("Updated DataFrame:")
    st.dataframe(df)
    if st.button('Refresh Data'):
    # Your data fetching logic here
        with open("default.json", 'w') as file:
            df.to_json("default.json", orient='records')
        st.write('Data refreshed!')
        
    return df
   
    
df = manage_sites(st.session_state["default_df"])
st.session_state["default_df"]=df

  