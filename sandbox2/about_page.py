import streamlit as st

def app():
    st.title("About Page")
    st.write("This is the About Page.")
    
    # Buttons for navigation
    if st.button('Go to Home Page'):
        st.session_state.current_page = 'Home'
        st.rerun()
    if st.button('Go to Contact Page'):
        st.session_state.current_page = 'Contact'
        st.rerun()
    