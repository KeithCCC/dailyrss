import streamlit as st

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠")

# Function to redirect to a different page
def navigate_to_page(page_name):
    st.text(st.query_params.page) 
    st.query_params.page = page_name

# Read the current query parameters
query_params = st.query_params
page = query_params.get("page", ["home"])[0]

st.title("Home Page")
st.write("Welcome to the Home Page!")

# Button to redirect to Page 1
if st.button("Go to Page 1"):
    st.text(st.query_params.page) 
    navigate_to_page("Page1")

# Button to redirect to Page 2
if st.button("Go to Page 2"):
    st.text(st.query_params.page)
    navigate_to_page("Page2")
