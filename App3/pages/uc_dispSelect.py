# list all collection site
# user select 
# feedparse each selected url
import pandas as pd
import os
import streamlit as st

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
            label = row['label']
            checkbox_key = f"checkbox_{index}"
            rulname = f"({label}) : {url}"
            st.session_state.checkbox_states[url] = st.checkbox(label=rulname, key=checkbox_key)

        submitted = st.form_submit_button("Check url")

        if submitted:
            st.text(st.session_state.checkbox_states)
            #TODO: add to currrent db and save
