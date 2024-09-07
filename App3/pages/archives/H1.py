import streamlit as st

st.title("Home Page")

if "A" not in st.session_state:
    st.session_state.A = 0

x = st.number_input("set A")
if st.button("set A"):
    st.session_state.A= x
st.text(st.session_state.A )
st.page_link("h1.py", label="Home", icon="🏠")
st.page_link("pages/p1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/p2.py", label="Page 2", icon="2️⃣")
st.page_link("http://www.google.com", label="Google", icon="🌎")