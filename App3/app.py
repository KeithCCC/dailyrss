from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json



if "df" not in st.session_state:
    # st.session_state["df"] = ""   
    filename = "default.json"
    if not os.path.exists(filename):
        st.text('default json does not exist')
        st.page_link("pages/firstData.py", label="Create data", icon="1️⃣")
    else:
        st.text('default json exist')
        df = pd.read_json(filename)
    st.session_state["df"] = df
    
st.data_editor(st.session_state.df)
