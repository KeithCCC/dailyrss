#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd

def manage_sites():
    st.title("Manage tech feeds")
    
    if "default_df" not in st.session_state:
        st.session_state["default_df"] = ""
        default_df = 'empty'
    else:
        default_df=st.session_state["default_df"]
    
    # print("show sites:" + st.session_state["default_df"])

    # st.table(sites[["uid", "Type", "Title", "URL", "URI", "Description"]])
    st.table(default_df)
    
    # Add a new row
    st.write("Add a new site:")
    new_site_title = st.text_input("title")
    new_site_url = st.text_input("site url")
    new_site_uri = st.text_input("site uri")
    new_site_description = st.text_input("site new_site_description")
    # new_age = st.text_input("Age", min_value=0, max_value=100)

    if st.button("Add site"):
        if new_site_url:
            new_row = pd.DataFrame({'Title': [new_site_title],'URL': [new_site_url], 'URI': [new_site_uri], 'Description': [new_site_description]})
            st.session_state.default_df = pd.concat([st.session_state.default_df, new_row], ignore_index=True)
            # st.experimental_user()

    st.write("Remove a site:")
    row_to_delete = st.selectbox("Select row to delete", st.session_state.default_df.index)

    if st.button("Delete Row"):
        if row_to_delete in st.session_state.default_df.index:
            st.session_state.default_df = st.session_state.default_df.drop(index=row_to_delete).reset_index(drop=True)
            # st.experimental_user()

    # Display the updated DataFrame
    st.write("Updated DataFrame:")
    st.dataframe(default_df)
    if st.button('Refresh Data'):
    # Your data fetching logic here
        filename = "default.json"
        with open(filename, 'w') as file:
            default_df.to_json(filename, orient='records')
        st.write('Data refreshed!')
    
    
manage_sites()