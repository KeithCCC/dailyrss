import flet as ft
import os
import pandas as pd
import json
import feedparser
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SITE_TITLE = "Daily RSS Reader"

class RSSReader(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.new_feed = ft.TextField(hint_text="Enter RSS feed URL", expand=True)
        self.feeds_view = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Label")),
                ft.DataColumn(ft.Text("Title")),
                ft.DataColumn(ft.Text("URL")),
                ft.DataColumn(ft.Text("Actions")),
            ],
            rows=[]
        )

    def build(self):
        return ft.Column([
            ft.Text(SITE_TITLE, size=24, weight=ft.FontWeight.BOLD),
            ft.Row([
                self.new_feed,
                ft.ElevatedButton("Add Feed", on_click=self.add_feed)
            ]),
            ft.ElevatedButton("View All Feeds", on_click=self.view_all_feeds),
            ft.ElevatedButton("Test URL for RSS", on_click=self.test_url),
            ft.ElevatedButton("Select Labels", on_click=self.select_labels),
            self.feeds_view
        ])

    def add_feed(self, e):
        label = "New Feed"  # You might want to add a TextField for this
        title = "New Feed Title"  # You might want to add a TextField for this
        url = self.new_feed.value
        self.save_feed(label, title, url)
        self.load_feeds()

    def view_all_feeds(self, e):
        # Implement view all feeds logic here
        pass

    def test_url(self, e):
        # Implement test URL logic here
        pass

    def select_labels(self, e):
        # Implement select labels logic here
        pass

    def load_feeds(self):
        filename = "default.json"
        if os.path.exists(filename):
            df = pd.read_json(filename)
            self.feeds_view.rows = [
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(row['label'])),
                    ft.DataCell(ft.Text(row['title'])),
                    ft.DataCell(ft.Text(row['URL'])),
                    ft.DataCell(
                        ft.Row([
                            ft.IconButton(ft.icons.EDIT, on_click=lambda _: self.edit_feed(index)),
                            ft.IconButton(ft.icons.DELETE, on_click=lambda _: self.delete_feed(index)),
                            ft.IconButton(ft.icons.VISIBILITY, on_click=lambda _: self.view_feed(index))
                        ])
                    )
                ]) for index, row in df.iterrows()
            ]
            self.update()

    def save_feed(self, label, title, url):
        filename = "default.json"
        if os.path.exists(filename):
            df = pd.read_json(filename)
        else:
            df = pd.DataFrame(columns=['label', 'title', 'URL'])
        
        new_row = pd.DataFrame({'label': [label], 'title': [title], 'URL': [url]})
        df = pd.concat([df, new_row], ignore_index=True)
        df = df.sort_values(by=['label', 'title'])
        df.to_json(filename, orient='records', force_ascii=False, encoding='utf-8')

    def edit_feed(self, index):
        # Implement edit feed logic here
        pass

    def delete_feed(self, index):
        filename = "default.json"
        if os.path.exists(filename):
            df = pd.read_json(filename)
            df = df.drop(df.index[index])
            df.to_json(filename, orient='records', force_ascii=False)
            self.load_feeds()

    def view_feed(self, index):
        # Implement view single feed logic here
        pass

def main(page: ft.Page):
    page.title = SITE_TITLE
    page.theme_mode = ft.ThemeMode.LIGHT
    
    rss_reader = RSSReader()
    page.add(rss_reader)
    rss_reader.load_feeds()

ft.app(target=main)
import flet as ft
import os
import pandas as pd
import json
import feedparser
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SITE_TITLE = "Daily RSS Reader"

class RSSReader(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.new_feed = ft.TextField(hint_text="Enter RSS feed URL", expand=True)
        self.feeds_view = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Label")),
                ft.DataColumn(ft.Text("Title")),
                ft.DataColumn(ft.Text("URL")),
                ft.DataColumn(ft.Text("Actions")),
            ],
            rows=[]
        )

    def build(self):
        return ft.Column([
            ft.Text(SITE_TITLE, size=24, weight=ft.FontWeight.BOLD),
            ft.Row([
                self.new_feed,
                ft.ElevatedButton("Add Feed", on_click=self.add_feed)
            ]),
            ft.ElevatedButton("View All Feeds", on_click=self.view_all_feeds),
            ft.ElevatedButton("Test URL for RSS", on_click=self.test_url),
            ft.ElevatedButton("Select Labels", on_click=self.select_labels),
            self.feeds_view
        ])

    def add_feed(self, e):
        label = "New Feed"  # You might want to add a TextField for this
        title = "New Feed Title"  # You might want to add a TextField for this
        url = self.new_feed.value
        self.save_feed(label, title, url)
        self.load_feeds()

    def view_all_feeds(self, e):
        # Implement view all feeds logic here
        pass

    def test_url(self, e):
        # Implement test URL logic here
        pass

    def select_labels(self, e):
        # Implement select labels logic here
        pass

    def load_feeds(self):
        filename = "default.json"
        if os.path.exists(filename):
            df = pd.read_json(filename)
            self.feeds_view.rows = [
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(row['label'])),
                    ft.DataCell(ft.Text(row['title'])),
                    ft.DataCell(ft.Text(row['URL'])),
                    ft.DataCell(
                        ft.Row([
                            ft.IconButton(ft.icons.EDIT, on_click=lambda _: self.edit_feed(index)),
                            ft.IconButton(ft.icons.DELETE, on_click=lambda _: self.delete_feed(index)),
                            ft.IconButton(ft.icons.VISIBILITY, on_click=lambda _: self.view_feed(index))
                        ])
                    )
                ]) for index, row in df.iterrows()
            ]
            self.update()

    def save_feed(self, label, title, url):
        filename = "default.json"
        if os.path.exists(filename):
            df = pd.read_json(filename)
        else:
            df = pd.DataFrame(columns=['label', 'title', 'URL'])
        
        new_row = pd.DataFrame({'label': [label], 'title': [title], 'URL': [url]})
        df = pd.concat([df, new_row], ignore_index=True)
        df = df.sort_values(by=['label', 'title'])
        df.to_json(filename, orient='records', force_ascii=False, encoding='utf-8')

    def edit_feed(self, index):
        # Implement edit feed logic here
        pass

    def delete_feed(self, index):
        filename = "default.json"
        if os.path.exists(filename):
            df = pd.read_json(filename)
            df = df.drop(df.index[index])
            df.to_json(filename, orient='records', force_ascii=False)
            self.load_feeds()

    def view_feed(self, index):
        # Implement view single feed logic here
        pass

def main(page: ft.Page):
    page.title = SITE_TITLE
    page.theme_mode = ft.ThemeMode.LIGHT
    
    rss_reader = RSSReader()
    page.add(rss_reader)
    rss_reader.load_feeds()

ft.app(target=main)