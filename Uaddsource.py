from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json



initial_data = [[0,"source", "@IT", "https://atmarkit.itmedia.co.jp/", "https://atmarkit.itmedia.co.jp/", "Atmark IT"]]
data_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description"])

filename = "default.json"
if not os.path.exists(filename):
    with open(filename, 'w') as file:
        data_df.to_json(filename, orient='records')
else:
    data_df = pd.read_json(filename)
    
st.table(data_df)
    
