from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json


# if "df" not in st.session_state:
    # st.session_state["df"] = ""   
filename = "default.json"
if not os.path.exists(filename):
    st.text('default json does not exist')
    st.page_link("pages/firstData.py", label="Create data", icon="1️⃣")
else:
    st.text('default json exist')
    df = pd.read_json(filename)
    df_sorted = df.sort_values(by='label', ascending=False)
    with open(filename, 'w') as file:
        df_sorted.to_json(filename, orient='records')
    st.session_state["df"] = df



# st.data_editor(st.session_state.df)

# Define the desired column order
custom_order = ['title', 'label', 'URL']

# Display the dataframe with custom column order
st.dataframe(df_sorted, column_order=custom_order)

#todo: disp filter by label
#todo: disp filter today
