import streamlit as st
from st_pages import Page, show_pages

pages = [
        Page("showPageDemo.py", "Home", "🏠"),
        Page("pages/page1.py", "Custom Name for Page 1", ":books:"),
    ]
show_pages(pages)