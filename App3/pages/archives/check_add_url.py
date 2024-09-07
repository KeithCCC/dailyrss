import streamlit as st
import re
import requests
from bs4 import BeautifulSoup

def extract_urls(website_url):
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
    
def is_rdf_extension(url):
    # Check if the URL ends with '.xml'
    return url.lower().endswith('.rdf')

def test_url(url):
    list_url = []
    st.text(f'test url:{url}')
    # if is_valid_url(url):   
    # st.text('valid url')
    if is_rdf_extension(url):
        st.text("rdf")
        list_url.append('URL')
    else:
        st.text("not rdf")
        list_url = extract_urls(url)
    # else:
    #     st.text('not valid url')
    return list_url

st.title("exp: Add new sits or rss")

if 'checkbox_states' not in st.session_state:
    st.session_state.checkbox_states = {}

message = "site or rss url"

# Add a new row
st.write("Add a new site:")
new_site_url = st.text_input(message)
new_site_label = st.text_input("site label")

# if 'rss_feeds' not in st.session_state:
st.session_state.rss_feeds = []
    
with st.form("my_form"):

    st.session_state.rss_feeds = test_url(new_site_url)
    st.text(new_site_url)
    st.text(st.session_state.rss_feeds)

    for index, item in enumerate(st.session_state.rss_feeds):
        link = item[1]  # Assuming item is a tuple or list and the first element is the label
        checkbox_key = f"checkbox_{index}"
        st.session_state.checkbox_states[link] = st.checkbox(label=link, key=checkbox_key)

    submitted = st.form_submit_button("Check url")

    if submitted:
        st.text(st.session_state.checkbox_states)
        #TODO: add to currrent db and save
