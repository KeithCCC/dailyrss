# input url
# test url
# add single url to collection
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_url_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        return title
    except requests.exceptions.RequestException as e:
        return []  # Return an empty list if there's an error

st.title("Add one RSS to collection")


url = st.text_input("URLを入力してください")
label = st.text_input("ラベルを入力してください")

if st.button("RSSを追加"):
    filename = os.path.join('.', 'default.json')
    df = pd.read_json(filename)
    
    already_exist = df['URL'].isin([url]).any()
    title = get_url_title(url)

    if already_exist:
        st.text(f"{title} はすでに登録されています")
    else:
        new_row = pd.DataFrame({'URL': [url], 'label': [label], 'title': [title]})
        df = pd.concat([df, new_row], ignore_index=True)

        with open(filename, 'w') as file:
            df.to_json(filename, orient='records')
        st.text("追加しました")
