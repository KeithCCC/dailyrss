import streamlit as st



st.title("Enter site to extract RSS feed")
#url = st.text_input("Site URL", "https://atmarkit.itmedia.co.jp/")

url = st.text_input("Site URL", "https://atmarkit.itmedia.co.jp/")
submit = st.button("Submit")
cancel = st.button("Cancel")

st.text(url)
if submit:
    #source_site = url
    st.session_state.source_site = url

