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


if 'df1' not in st.session_state:
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Occupation': ['Engineer', 'Doctor', 'Artist']
    }
    st.session_state.df1 = pd.DataFrame(data)

if 'df' not in st.session_state:
    st.session_state.df = sample_df()

st.text(st.session_state.df)
message = "site or rss url"

# Add a new row
st.write("Add a new site:")
new_site_url = st.text_input(message)
new_site_label = st.text_input("site label")

if st.button("Add site"):
    rss_feeds = []
    if is_valid_url(new_site_url):
        st.text(new_site_url)
        if is_rdf_extension(new_site_url):
            rss_feeds.append('URL')
        else:
            rss_feeds = extract_urls_title(new_site_url)
            
        for row in rss_feeds:
            col1, col2 = st.columns([3, 1])  # Adjust the proportions as needed

            with col1:
                st.write(row[0],row[1])

            # Display the first action button in the second column
            with col2:
                if st.button("add", key=f"add_key{row}"):
                    st.text("key:",f"Added add_key{row}")
                    #to do add to df
                    # print(f"Added add_key{row}",new_site_label,new_site_url)
                    # new_row = pd.DataFrame({'label': [row[0]],'URL': [row[1]], 'URI': [row[1]]})
                    # # st.dataframe(new_row)
                    # st.session_state.df  = pd.concat([st.session_state.df , new_row], ignore_index=True)
                    # st.text(st.session_state.df )
                    # print (st.session_state.df )
                    
                    


    else:
        message = "Enter site or rss url again"

st.dataframe(st.session_state.df)

    # st.write("Updated DataFrame:")
    # st.dataframe(df)
    # if st.button('Refresh Data'):
    #     st.dataframe(df)
#Your data fetching logic here
with open("default.json", 'w') as file:
    st.session_state.df.to_json("default.json", orient='records')
# st.write('Data refreshed!')

    # return df
   
    
# df = manage_sites(st.session_state["default_df"])
# st.session_state["default_df"]=df

  