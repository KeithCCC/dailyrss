#Read all url from default.json
#display using feedparser with looping
import streamlit as st
import os
import pandas as pd
import feedparser
from bs4 import BeautifulSoup

st.title("Display All")

filename = os.path.join('.', 'default.json')
if not os.path.exists(filename):
    st.text('Could not read data')
    st.page_link("pages/firstData.py", label="Click here to create data", icon="1️⃣")

else:
    st.text('Read saved data')
    df = pd.read_json(filename)
    # st.data_editor(df)
    
    try:
        for index, row in df.iterrows():
            url = row['URL']
            label = row['label']
            st.markdown(
                """
                <style>
                .red-text {
                    color: red;
                    font-size: 20px;  /* Adjust the size as needed */
                }
                .blue-text {
                    color: blue;
                    font-size: 20px;  /* Adjust the size as needed */
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            title_line = f"({label}) \n {row['title']})"
            title_line2 = f"({url})"
            biggerfontstr =  f'<p class="blue-text"> {title_line}!</p>'
            biggerfontstr2 =  f'<p class="red-text"> {title_line2}!</p>'
            st.markdown(biggerfontstr, unsafe_allow_html=True)
            st.markdown(biggerfontstr2, unsafe_allow_html=True)
            st.markdown(
                """
                <style>
                .custom-divider {
                    border-top: 3px solid #ff6347;  /* Change color and thickness */
                    margin: 25px 0;  /* Adjust spacing */
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
            feed = feedparser.parse(url)
            for entry in feed.entries:
                outputstr = ""
                if  'title' in entry:
                    outputstr += entry.title
                if 'published' in entry:
                    outputstr += "(" + entry.published + ")"
                    # st.write(entry.published)
                # st.write(entry.title)
                # st.markdown(f"[click]({entry.link})", unsafe_allow_html=True)
                if 'summry' in entry:
                    outputstr += "Summary:" + entry.summary
                # outputstr += "  "  + f"[click]({entry.link})" 
                st.markdown(outputstr, unsafe_allow_html=True)
        
                st.write(f"[click]({entry.link})")
                st.markdown("---")

    except Exception as e:
        st.error(f"An error occurred while processing {label}: {str(e)}")           
        # You can use st.markdown to make the URL clickable
        # st.markdown(f"[Click here to visit]({url})")
        
        # Optionally, you can add a separator between URLs
        # st.markdown("---")