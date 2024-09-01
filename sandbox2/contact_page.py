import streamlit as st

def app():
    st.title("Contact Page")
    st.write("You can contact us at: contact@example.com")
    
    # Buttons for navigation
    if st.button('Go to Home Page'):
        st.session_state.current_page = 'Home'
        st.rerun()
    if st.button('Go to About Page'):
        st.session_state.current_page = 'About'
        st.rerun()