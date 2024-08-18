
from xml.etree import ElementTree
import streamlit  as st
import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
import os
import json


filename_news= "newsfeed.json"
news_df = pd.read_json(filename_news)

print(news_df)

