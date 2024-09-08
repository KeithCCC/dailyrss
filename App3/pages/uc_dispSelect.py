# list all collection site
# user select 
# feedparse each selected url
import pandas as pd
import os
import streamlit as st
import feedparser

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
            st.text(st.session_state.checkbox_states)
            #  for index in st.session_state.checkbox_states:
            #     if st.session_state.checkbox_states[index]:
            #         st.text(url)
            st.text(type(st.session_state.checkbox_states))
            #TODO: add to currrent db and save
            selected_df = df[df.index.isin([idx for idx, checked in st.session_state.checkbox_states.items() if checked])]
            st.dataframe(selected_df)

            try:
                    for index, row in selected_df.iterrows():
                        url = row['URL']
                        label = row['label']
                        col1, col2 = st.columns([1, 4])  # Adjust the ratio as needed
                
                        with col1:
                            st.write(f"({label}) \n {row['title']}\n {url}")
                        with col2:
                            feed = feedparser.parse(url)
                            for entry in feed.entries:
                                outputstr = ""
                                if  'title' in entry:
                                    outputstr += "Titl:" + entry.title
                                if 'published' in entry:
                                    outputstr += "(" + entry.published + ")"
                                    # st.write(entry.published)
                                # st.write(entry.title)
                                # st.markdown(f"[click]({entry.link})", unsafe_allow_html=True)
                                if 'summry' in entry:
                                    outputstr += "Summary:" + entry.summary
                                # outputstr += "  "  + f"[click]({entry.link})" 
                                st.markdown(outputstr, unsafe_allow_html=True)
                    
                                st.write(f"[click]({entry.link})")
                                st.markdown("---")

            except Exception as e:
                    st.error(f"An error occurred while processing {label}: {str(e)}") 