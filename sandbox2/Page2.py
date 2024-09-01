import streamlit as st

# Set page configuration
st.set_page_config(page_title="Page 2", page_icon="📑")

# Function to redirect to a different page
def navigate_to_page(page_name):
    st.text(st.query_params.page) 
    st.query_params.page = page_name

st.title("Page 2")
st.write("Welcome to Page 2!")

# Button to redirect back to Home Page
if st.button("Back to Home"):
    st.text(st.query_params.page)
    navigate_to_page("Home")
