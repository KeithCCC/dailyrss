#Read all url from default.json
#display using feedparser with looping
import streamlit as st
import os
import pandas as pd
import feedparser

st.title("Display All")

filename = os.path.join('.', 'default.json')
if not os.path.exists(filename):
    st.text('Could not read data')
    st.page_link("pages/firstData.py", label="Click here to create data", icon="1️⃣")

else:
    st.text('Read saved data')
    df = pd.read_json(filename)
    # st.data_editor(df)
    
    for index, row in df.iterrows():
        url = row['URL']
        label = row['label']
        st.write(f"({label}) URL {index + 1}: {url}")
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if  'title' in entry:
                st.write(entry.title)
            if 'published' in entry:
                st.write(entry.published)
            # st.write(entry.title)
            st.write(entry.link)
            if 'summry' in entry:
                st.write(entry.summary)
            st.write('---------------------------------')
        
        # You can use st.markdown to make the URL clickable
        # st.markdown(f"[Click here to visit]({url})")
        
        # Optionally, you can add a separator between URLs
        # st.markdown("---")