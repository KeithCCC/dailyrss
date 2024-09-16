from xml.etree import ElementTree
import streamlit as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json

st.title("Edit Collection")

filename = os.path.join('.', 'default.json')
df = pd.read_json(filename)

# Define column configuration to make columns wider and set custom order
column_config = {
    "title": st.column_config.TextColumn("Title", width="medium"),
    "label": st.column_config.TextColumn("Label", width="medium"),
    "URL": st.column_config.TextColumn("URL", width="medium"),
}

# Reorder the DataFrame columns
df = df[["title", "label", "URL"]]

df_changed = st.data_editor(df, column_config=column_config)
df_changed = df_changed.dropna(how='all')

if st.button("Save"):
    with open(filename, 'w') as file:
        df_changed.to_json(filename, orient='records')
    st.text("保存しました")
