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

st.session_state["selected_label"] = []

filename = os.path.join('.', 'default.json')
if not os.path.exists(filename):
    st.text('Could not read data')
    st.page_link("pages/firstData.py", label="Click here to create data", icon="1️⃣")

else:
    # st.text('Read saved data')
    df = pd.read_json(filename)
    # st.data_editor(df)
    
    unique_label_list = df['label'].unique().tolist()
    
    # st.write(unique_label_list)
    with st.form("select_form"):
        for index, label in unique_label_list:
            st.session_state.selected_label[index] = st.checkbox(label=label, key=label)
        submitted = st.form_submit_button("Submit")
        
        
        if submitted:
            selected_labels = [label for label, checked in st.session_state.selected_label.items() if checked]
            selected_df = df[df['label'].isin(selected_labels)]
            st.session_state['selected_df'] = selected_df
            st.write("Selected DataFrame:")
            st.dataframe(selected_df)
            
            if not selected_df.empty:
                switch_page("dispSelectOnly")
            else:
                st.warning("No labels selected. Please select at least one label.")

