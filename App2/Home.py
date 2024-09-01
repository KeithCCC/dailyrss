from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json

def sample_df():
    initial_data = [[0,"rss", "@IT", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "Atmark IT","Tech"]]
    sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description","label"])
    return sample_df 

def main():
    if "df" not in st.session_state:
        # st.session_state["df"] = ""   
        filename = "default.json"
        if not os.path.exists(filename):
            df = sample_df()
            with open(filename, 'w') as file:
                df.to_json(filename, orient='records')
        else:
            df = pd.read_json(filename)
        st.session_state["df"] = df