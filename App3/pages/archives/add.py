#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import re


st.title("add list")

site_list = st.session_state.df.values.tolist()

for row in site_list:
    col1, col2 = st.columns([3, 1])  # Adjust the proportions as needed
    with col1:
        st.write(row[0],row[1],row[2],row[3],row[4])
    # Display the first action button in the second column
    

if st.button("Add site"):
    st.session_state.add_site = True
    rss_feeds = []
    if is_valid_url(new_site_url):
        st.text(new_site_url)
        if is_rdf_extension(new_site_url):
            rss_feeds.append('URL')
        else:
            rss_feeds = extract_urls_title(new_site_url)
        
        cnt=0
        print(st.session_state.add_site)
        if st.session_state.add_site:
            for row in rss_feeds:
                col1, col2 = st.columns([3, 1])  # Adjust the proportions as needed
                cnt+=1
                with col1:
                    st.write(str(cnt) + " " + row[0],row[1])
                # Display the first action button in the second column
                with col2:
                    if st.button(f"add {cnt}", key=f"add_key{cnt}"):
                        st.session_state.target_site = row[1]
                        st.text("add site button clicked")
                        print(st.session_state.target_site)
                        print("add site button clicked")
                        st.write(st.session_state.target_site)
                        #to do add to df
                        # print(f"Added add_key{row}",new_site_label,new_site_url)
                        # new_row = pd.DataFrame({'label': [row[0]],'URL': [row[1]], 'URI': [row[1]]})
                        # # st.dataframe(new_row)
                        # st.session_state.df  = pd.concat([st.session_state.df , new_row], ignore_index=True)
                        # st.text(st.session_state.df )
                        # print (st.session_state.df )
                        
                        


    # else:
    #     message = "Enter site or rss url again"

    st.dataframe(st.session_state.df)

    # st.write("Updated DataFrame:")
    # st.dataframe(df)
    # if st.button('Refresh Data'):
    #     st.dataframe(df)
    #Your data fetching logic here
    # with open("default.json", 'w') as file:
    #     st.session_state.df.to_json("default.json", orient='records')
    # st.write('Data refreshed!')

    # return df
   
    
    # df = manage_sites(st.session_state["default_df"])
    # st.session_state["default_df"]=df

  