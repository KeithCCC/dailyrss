# list all collection site
# user select 
# feedparse each selected url
import pandas as pd
import os
import streamlit as st
import feedparser
from streamlit.runtime.scriptrunner import RerunData, RerunException
from streamlit.source_util import get_pages

def switch_page(page_name: str):
    page_name = page_name.lower()
    pages = get_pages("app.py")  # Adjust this to your main script name if different
    for page_hash, config in pages.items():
        if config["page_name"].lower() == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )
    page_names = [config["page_name"] for config in pages.values()]
    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

st.title("Display Select")

filename = os.path.join('.', 'default.json')
if not os.path.exists(filename):
    st.text('Could not read data')
    st.page_link("pages/firstData.py", label="Click here to create data", icon="1️⃣")

else:
    st.text('Read saved data')
    df = pd.read_json(filename)
    # st.data_editor(df)
    
    if 'checkbox_states' not in st.session_state:
        st.session_state.checkbox_states = {}
    
    with st.form("my_form"):
        for index, row in df.iterrows():
            url = row['URL']
            label = f"{row['label']} : {row['title']}"
            checkbox_key = f"checkbox_{index}"
            urlname = f"({label}) : {url}"
            st.session_state.checkbox_states[index] = st.checkbox(label=urlname, key=checkbox_key)
        submitted = st.form_submit_button("Submit")

        if submitted:
            # st.text(st.session_state.checkbox_states)
            #  for index in st.session_state.checkbox_states:
            #     if st.session_state.checkbox_states[index]:
            #         st.text(url)
            # st.text(type(st.session_state.checkbox_states))
            # TODO: add to currrent db and save
            selected_df = df[df.index.isin([idx for idx, checked in st.session_state.checkbox_states.items() if checked])]
            # st.dataframe(selected_df)
            st.session_state['selected_df'] = selected_df
            switch_page("dispSelectOnly")

