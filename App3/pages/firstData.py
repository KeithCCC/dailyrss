import pandas as pd
import os
import streamlit as st

def sample_df():
    initial_data = [[0,"rss", "@IT", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "https://rss.itmedia.co.jp/rss/1.0/ait.xml", "Atmark IT","Tech"]]
    sample_df = pd.DataFrame(initial_data, columns=["uid", "Type", "Title", "URL", "URI", "Description","label"])
    return sample_df 

def sample_df2():
#  ["label", "URL"]
    initial_data = ["https://rss.itmedia.co.jp/rss/1.0/ait.xml", "Tech"]
    sample_df = pd.DataFrame([initial_data], columns=["URL", "label"])
    return sample_df 


# sample_df2()

# filename = "default.json"
filename = os.path.join('.', 'default.json')
if not os.path.exists(filename):
    st.text('Create new data')
    df = sample_df2()
    with open(filename, 'w') as file:
        df.to_json(filename, orient='records')
        
else:
    st.text('Read saved data')
    df = pd.read_json(filename)