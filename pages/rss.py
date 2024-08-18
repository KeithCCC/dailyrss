#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os


# def sample_df():
#     initial_data = [[0,"rss", "@IT", "https://atmarkit.itmedia.co.jp/", "https://atmarkit.itmedia.co.jp/", "Atmark IT","Tech"]]
#     sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description","label"])
#     return sample_df

def rss_task(df):
    
    st.text('rss list')
    st.text(df)
    rss_show =""
    list_rss =[]
    
    for index, row in df.iterrows():
        # Create a new row with columns
        row_as_list = row.to_list()
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])  # Adjust the proportions as needed

        with col1:
            st.write(row_as_list[6]+":  "+row_as_list[3])

        # Display the first action button in the second column
        with col2:
            if st.button("rss"):
                rss_show = row_as_list[3]
                
        with col3:
            if st.button("rss today"):
                rss_show = row_as_list[3]
        
        with col4:
            if st.button(f"delete"):
                st.write(f"delet rss action")
    
    list_rss.append(rss_show)
    feed = feedparser.parse(rss_show)
    st.text(feed)
    for entry in feed.entries:
        if 'published' in entry:
            st.text(entry.published)
        st.write(entry.title)
        st.write(entry.link)
        st.write(entry.summary)
        st.text('---------------------------------')
             
                
    return df
            # if st.button("Add site"):
            #     if new_site_url:
            #     new_row = pd.DataFrame({'Title': [new_site_title],'URL': [new_site_url], 'URI': [new_site_uri], 'Description': [new_site_description]})
            #     st.session_state.default_df = pd.concat([st.session_state.default_df, new_row], ignore_index=True)
                # st.experimental_user()

            # Display the second action button in the third column

                    
# def rss():
#     # if "default_df" not in st.session_state:
#     #         st.session_state["default_df"] = ""

#     # filename = "default.json"
#     # if not os.path.exists(filename):
#     #     print('default.json not found')
#     #     default_df = sample_df()
#     #     with open(filename, 'w') as file:
#     #         default_df.to_json(filename, orient='records')
#     # else:
#     #     default_df = pd.read_json(filename)
    
#     # default_site_list = sites_df[sites_df['Type'] == 'source']

#     df = display_sites(st.session_state["default_df"])
#     st.session_state["default_df"]=df
    
df = rss_task(st.session_state["default_df"])
st.session_state["default_df"]=df

    