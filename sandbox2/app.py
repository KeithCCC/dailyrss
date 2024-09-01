import streamlit as st
from home_page import app as home_page
from about_page import app as about_page
from contact_page import app as contact_page

# Initialize session state if not already set
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

st.write(st.__version__)

# Function to render the current page based on session state
def run_page():
    if st.session_state.current_page == 'Home':
        home_page()
    elif st.session_state.current_page == 'About':
        about_page()
    elif st.session_state.current_page == 'Contact':
        contact_page()

# Run the app
run_page()
