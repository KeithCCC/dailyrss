from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json


st.text(st.session_state["a"])
st.text(st.session_state["b"])



st.dataframe(st.session_state.df1)

df= st.session_state.df1
df_list = df.values.tolist()

for item in df_list:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.text(item[0])
    with col2:
        st.text(item[1])
    with col3:
        st.text(item[2])
    with col4:
        if st.button("delete", key=item[0]):
            df_list.remove(item)
            print(df_list)
            st.text(df_list)
            # st.experimental_rerun()          

st.text(df_list)
if st.button("Refresh"):
    st.experimental_rerun()  # Make sure to call it correctly
# new_name = st.text_input("name")
# new_age = st.number_input("age")
# new_occupation = st.text_input("occupation")

# if st.button("Add person"):
#     newR = pd.DataFrame({"Name": [new_name], "Age": [new_age], "Occupation": [new_occupation]})
#     df = pd.concat([df, newR], ignore_index=True)

# st.dataframe(st.session_state.df1)
# print(df)