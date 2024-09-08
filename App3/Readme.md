New table
Type	Title	url	uri	description
source or rss	Text	link	link	Text


https://news.yahoo.co.jp/rss/topics/top-picks.xml


https://win-tab.net/feed/
https://win-tab.net/
https://pc.watch.impress.co.jp/
https://pc.watch.impress.co.jp/data/rss/1.0/pcw/feed.rdf
https://pc.watch.impress.co.jp/data/rss/1.0/pcw/feed.rdf


        with col2:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    outputstr = ""
                    if  'title' in entry:
                        outputstr += "Titl:" + entry.title
                    if 'published' in entry:
                        outputstr += "(" + entry.published + ")"
                        # st.write(entry.published)
                    # st.write(entry.title)
                    # st.markdown(f"[click]({entry.link})", unsafe_allow_html=True)
                    if 'summry' in entry:
                        outputstr += "Summary:" + entry.summary
                    st.markdown(outputstr, unsafe_allow_html=True)
                    st.markdown("---")   
            except Exception as e:
                st.error(f"An error occurred while processing {label}: {str(e)}")           


    outputstr += "  "  + f"[click]({entry.link})"  