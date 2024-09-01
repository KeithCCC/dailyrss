from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json


st.title("session state teste")


st.session_state["a"] = "AAA"
st.session_state["b"] = "BBB"

if 'df1' not in st.session_state:
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'keith'],
        'Age': [25, 30, 35, 55],
        'Occupation': ['Engineer', 'Doctor', 'Artist', 'king']
    }
    st.session_state.df1 = pd.DataFrame(data)