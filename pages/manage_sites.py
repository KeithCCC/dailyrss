#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os


def sample_df():
    initial_data = [[0,"rss", "@IT", "https://atmarkit.itmedia.co.jp/", "https://atmarkit.itmedia.co.jp/", "Atmark IT"]]
    sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description"])
    return sample_df

def display_sites(df):
    
    st.button('Add new site')
    
    for index, row in df.iterrows():
        # Create a new row with columns
        row_as_list = row.to_list()
        col1, col2, col3 = st.columns([2, 1, 1])  # Adjust the proportions as needed

        if row_as_list[1] == 'source':
            # Display the item in the first column
            with col1:
                st.write(row_as_list[3])

            # Display the first action button in the second column
            with col2:
                if st.button(f"Action 1 for {index}"):
                    st.write(f"Action 1 triggered for {index}")

            # Display the second action button in the third column
            with col3:
                if st.button(f"Action 2 for {index}"):
                    st.write(f"Action 2 triggered for {index}")

if "sites_df" not in st.session_state:
        st.session_state["sites_df"] = ""
if "news_df" not in st.session_state:
        st.session_state["news_df"] = ""
       
filename = "default.json"
if not os.path.exists(filename):
    print('default.json not found')
    sites_df = sample_df()
    with open(filename, 'w') as file:
        sites_df.to_json(filename, orient='records')
else:
    sites_df = pd.read_json(filename)

filename_news= "newsfeed.json"
if not os.path.exists(filename_news):
    print('newsfeed.json not found')
    news_df = sample_df()
    with open(filename_news, 'w') as file:
        news_df.to_json(filename_news, orient='records')
else:
    news_df = pd.read_json(filename_news)
    
# default_site_list = sites_df[sites_df['Type'] == 'source']

display_sites(sites_df)

# print(sites_df)
# print(news_df)

