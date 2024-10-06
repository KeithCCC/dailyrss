import flet as ft
import pandas as pd
import requests
import json

# Load RSS feed addresses from JSON
def load_feeds():
    with open('feeds.json', 'r') as file:
        return json.load(file)

# Fetch RSS feed articles
def fetch_rss(url):
    response = requests.get(url)
    return response.text  # You can parse this with an XML parser

# Main application function
def main(page: ft.Page):
    page.title = "RSS Feed Reader"
    
    # Load feeds
    feeds = load_feeds()
    feed_names = [feed['name'] for feed in feeds]
    
    # Dropdown for selecting feeds
    feed_dropdown = ft.Dropdown(label="Select RSS Feed", options=[ft.dropdown.Option(name) for name in feed_names])
    page.add(feed_dropdown)

    # Display area for articles
    articles_container = ft.Column()
    page.add(articles_container)

    # Function to display articles
    def display_articles(e):
        selected_feed = feed_dropdown.value
        feed_url = next(feed['url'] for feed in feeds if feed['name'] == selected_feed)
        rss_content = fetch_rss(feed_url)
        
        # Here you would parse the RSS content and extract articles
        # For demonstration, we will just add a placeholder
        articles_container.controls.append(ft.Text(f"Articles from {selected_feed}:"))
        articles_container.controls.append(ft.Text(rss_content))  # Replace with parsed articles
        page.update()

    feed_dropdown.on_change = display_articles

    # Add functionality for adding, editing, and deleting feeds (not implemented in this snippet)

ft.app(target=main)