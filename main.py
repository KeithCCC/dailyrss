from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json

class rsss_feed:
    def __init__(self, source_site_name, title, url, uri, created_date):
        self.source_site_name = source_site_name
        self.title = title
        self.url = url
        self.uri = uri
        self.created_date = created_date
        
    def __repr__(self):
        return f"rsss_feed(title={self.title}, url={self.url})"

class source_site:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        
    def __repr__(self):
        return f"source_site(titel={self.title}, url={self.url})"
    
    def add_rss_feed(self, rss_feed):
        self.children.append(rss_feed)

# def sample_df():
#     initial_data = [[0,"source", "@IT", "https://atmarkit.itmedia.co.jp/", "https://atmarkit.itmedia.co.jp/", "Atmark IT"]]
#     sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description"])
#     return sample_df

def sample_df():
    initial_data = [[0,"rss", "@IT", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "Atmark IT","Tech"]]
    sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description","label"])
    return sample_df 

def main():
    if "default_df" not in st.session_state:
        # st.session_state["default_df"] = ""
        filename = "default.json"
        if not os.path.exists(filename):
            default_df = sample_df()
            with open(filename, 'w') as file:
                default_df.to_json(filename, orient='records')
        else:
            default_df = pd.read_json(filename)
        st.session_state["default_df"] = default_df
        
        print(default_df)
    
    # filename_news= "newsfeed.json"
    # if not os.path.exists(filename_news):
    #     news_df = sample_df()
    #     with open(filename_news, 'w') as file:
    #         news_df.to_json(filename_news, orient='records')
    # else:
    #     news_df = pd.read_json(filename_news)
        
    # filename_tech= "techfeed.json"
    # if not os.path.exists(filename_tech):
    #     with open(filename_tech, 'w') as file:
    #         tech_df.to_json(filename_tech, orient='records')
    # else:
    #     sites_df = pd.read_json(filename_tech)
        
    
    
    # st.session_state.news_df = news_df
   

    st.title("rss reader") 
    
    st.text("rss")
    st.text(st.session_state.default_df)
    st.text("---------------------------")
    st.text(st.session_state["default_df"])
    # st.text("News")
    # st.text(st.session_state.news_df)
    if st.button("Reset data"):
        default_df = sample_df()
        with open("default.json", 'w') as file:
            default_df.to_json("default.json", orient='records')
            st.session_state["default_df"] = default_df


main()
#if __name__ == "__mainRF1__":
