import streamlit as st

def app():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    
    # Buttons for navigation
    if st.button('Go to About Page'):
        st.session_state.current_page = 'About'
        st.rerun()
    if st.button('Go to Contact Page'):
        st.session_state.current_page = 'Contact'
        st.rerun()