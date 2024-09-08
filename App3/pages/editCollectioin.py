from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json

st.title("Edit Collection")

#todo: 
# 1. remove from list
# 2. edit lable
# 3. edit url
# 4. save
filename = os.path.join('.', 'default.json')
df = pd.read_json(filename)
df_changed = st.data_editor(df)
df_changed = df_changed.dropna(how='all')

if st.button("Save"):
    with open(filename, 'w') as file:
        df_changed.to_json(filename, orient='records')
    st.text("保存しました")
