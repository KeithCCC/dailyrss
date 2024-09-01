import streamlit as st

# Initialize session state for current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Function to navigate to different pages
def navigate(page_name):
    st.session_state.current_page = page_name

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Update the current page based on sidebar selection
navigate(page)

# Define each page's content
def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def about_page():
    st.title("About Page")
    st.write("This is the About Page.")

def contact_page():
    st.title("Contact Page")
    st.write("You can contact us at: contact@example.com")

# Display the content of the selected page
if st.session_state.current_page == 'Home':
    home_page()
elif st.session_state.current_page == 'About':
    about_page()
elif st.session_state.current_page == 'Contact':
    contact_page()
