##################################################
# RSS reader
##################################################

#import extractrss
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
from datetime import datetime 


def extract_rss_urls(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rss_urls = []
    for link in soup.find_all('link', type='application/rss+xml'):
        rss_urls.append(link.get('href'))

    return rss_urls

def ShowFeed():
    try:
        if "sites_df" not in st.session_state:
            st.session_state["sites_df"] = ""
            sites_df = 'empty'
        else:
            sites_df=st.session_state["sites_df"]
            
        st.title("Select tech site to read feeds")
        st.table(sites_df)

        row_to_select = st.selectbox("Select site", st.session_state.sites_df.index)


        col1, col2 = st.columns(2)
        with col1:
            btn_sel = st.button("Select")
            
        with col2:
            btn_today = st.button("Today")

        if btn_sel:
            if row_to_select in st.session_state.sites_df.index:
                rss_feeds = extract_rss_urls(sites_df.loc[row_to_select, 'URL'])
            for item in rss_feeds:
                feed = feedparser.parse(item)
                for entry in feed.entries:
                    # st.write(entry.link)
                    if 'published' in entry:
                        st.text(entry.published)
                    title_line =f"<p style='font-size:18px; color:yellow;'>{entry.title}</p>"
                    st.markdown(title_line,  unsafe_allow_html=True)
                    st.write(entry.summary)
                    st.write(entry.link)
                    st.text('---------------------------------')
        
        if btn_today:
            if row_to_select in st.session_state.sites_df.index:
                rss_feeds = extract_rss_urls(sites_df.loc[row_to_select, 'URL'])
            for item in rss_feeds:
                feed = feedparser.parse(item)
                for entry in feed.entries:
                    if 'published' in entry:
                        published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z').date()
                        if published_date == datetime.today().date():
                            st.text(entry.published)
                            title_line =f"<p style='font-size:18px; color:yellow;'>{entry.title}</p>"
                            st.markdown(title_line,  unsafe_allow_html=True)                
                            st.write(entry.summary)
                            st.write(entry.link)
                            st.text('---------------------------------')
    except Exception as e:
        pass            
 
    #rss_feeds = extract_rss_urls(st.session_state["source"]["url"])
    # rss_feeds = extract_rss_urls(st.session_state.sample_url)

            
    

    
ShowFeed()
# if __name__ == "__main__":
