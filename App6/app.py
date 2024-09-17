import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import feedparser
import os
import json

class RSSFeedManager:
    def __init__(self, root):
        self.root = root
        self.root.title("RSS Feed Manager")
        self.filename = "default.json"
        
        self.create_widgets()
        self.load_feeds()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.add_feed_button = tk.Button(self.frame, text="Add New Feed", command=self.add_feed)
        self.add_feed_button.grid(row=0, column=0, padx=5)

        self.view_feeds_button = tk.Button(self.frame, text="View All Feeds", command=self.view_feeds)
        self.view_feeds_button.grid(row=0, column=1, padx=5)

        self.select_labels_button = tk.Button(self.frame, text="Select Labels", command=self.select_labels)
        self.select_labels_button.grid(row=0, column=2, padx=5)

        self.find_feeds_button = tk.Button(self.frame, text="Find Feeds", command=self.find_feeds)
        self.find_feeds_button.grid(row=0, column=3, padx=5)

        self.end_program_button = tk.Button(self.frame, text="End Program", command=self.end_program, bg="#f44336")
        self.end_program_button.grid(row=0, column=4, padx=5)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=10)

    def load_feeds(self):
        if os.path.exists(self.filename):
            try:
                self.df = pd.read_json(self.filename)
                self.display_feeds()
            except Exception as e:
                messagebox.showerror("Error", f"Error processing data: {str(e)}")
        else:
            self.df = pd.DataFrame(columns=['label', 'title', 'URL'])
            self.display_feeds()

    def display_feeds(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        if not self.df.empty:
            for index, row in self.df.iterrows():
                tk.Label(self.table_frame, text=row['label']).grid(row=index, column=0, padx=5, pady=5)
                tk.Label(self.table_frame, text=row['title']).grid(row=index, column=1, padx=5, pady=5)
                tk.Label(self.table_frame, text=row['URL']).grid(row=index, column=2, padx=5, pady=5)
                tk.Button(self.table_frame, text="View", command=lambda i=index: self.view_feed(i)).grid(row=index, column=3, padx=5, pady=5)
                tk.Button(self.table_frame, text="Edit", command=lambda i=index: self.edit_feed(i)).grid(row=index, column=4, padx=5, pady=5)
                tk.Button(self.table_frame, text="Delete", command=lambda i=index: self.delete_feed(i)).grid(row=index, column=5, padx=5, pady=5)
        else:
            tk.Label(self.table_frame, text="No feeds available.").pack()

    def add_feed(self):
        # Implement the logic to add a new feed
        pass

    def view_feeds(self):
        # Implement the logic to view all feeds
        pass

    def select_labels(self):
        # Implement the logic to select labels
        pass

    def find_feeds(self):
        # Implement the logic to find feeds
        pass

    def end_program(self):
        self.root.quit()

    def view_feed(self, index):
        # Implement the logic to view a single feed
        pass

    def edit_feed(self, index):
        # Implement the logic to edit a feed
        pass

    def delete_feed(self, index):
        if messagebox.askyesno("Delete Feed", "Are you sure you want to delete this feed?"):
            self.df = self.df.drop(index)
            self.df.to_json(self.filename, orient='records')
            self.load_feeds()

if __name__ == "__main__":
    root = tk.Tk()
    app = RSSFeedManager(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import feedparser
import os
import json

class RSSFeedManager:
    def __init__(self, root):
        self.root = root
        self.root.title("RSS Feed Manager")
        self.filename = "default.json"
        
        self.create_widgets()
        self.load_feeds()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.add_feed_button = tk.Button(self.frame, text="Add New Feed", command=self.add_feed)
        self.add_feed_button.grid(row=0, column=0, padx=5)

        self.view_feeds_button = tk.Button(self.frame, text="View All Feeds", command=self.view_feeds)
        self.view_feeds_button.grid(row=0, column=1, padx=5)

        self.select_labels_button = tk.Button(self.frame, text="Select Labels", command=self.select_labels)
        self.select_labels_button.grid(row=0, column=2, padx=5)

        self.find_feeds_button = tk.Button(self.frame, text="Find Feeds", command=self.find_feeds)
        self.find_feeds_button.grid(row=0, column=3, padx=5)

        self.end_program_button = tk.Button(self.frame, text="End Program", command=self.end_program, bg="#f44336")
        self.end_program_button.grid(row=0, column=4, padx=5)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=10)

    def load_feeds(self):
        if os.path.exists(self.filename):
            try:
                self.df = pd.read_json(self.filename)
                self.display_feeds()
            except Exception as e:
                messagebox.showerror("Error", f"Error processing data: {str(e)}")
        else:
            self.df = pd.DataFrame(columns=['label', 'title', 'URL'])
            self.display_feeds()

    def display_feeds(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        if not self.df.empty:
            for index, row in self.df.iterrows():
                tk.Label(self.table_frame, text=row['label']).grid(row=index, column=0, padx=5, pady=5)
                tk.Label(self.table_frame, text=row['title']).grid(row=index, column=1, padx=5, pady=5)
                tk.Label(self.table_frame, text=row['URL']).grid(row=index, column=2, padx=5, pady=5)
                tk.Button(self.table_frame, text="View", command=lambda i=index: self.view_feed(i)).grid(row=index, column=3, padx=5, pady=5)
                tk.Button(self.table_frame, text="Edit", command=lambda i=index: self.edit_feed(i)).grid(row=index, column=4, padx=5, pady=5)
                tk.Button(self.table_frame, text="Delete", command=lambda i=index: self.delete_feed(i)).grid(row=index, column=5, padx=5, pady=5)
        else:
            tk.Label(self.table_frame, text="No feeds available.").pack()

    def add_feed(self):
        # Implement the logic to add a new feed
        pass

    def view_feeds(self):
        # Implement the logic to view all feeds
        pass

    def select_labels(self):
        # Implement the logic to select labels
        pass

    def find_feeds(self):
        # Implement the logic to find feeds
        pass

    def end_program(self):
        self.root.quit()

    def view_feed(self, index):
        # Implement the logic to view a single feed
        pass

    def edit_feed(self, index):
        # Implement the logic to edit a feed
        pass

    def delete_feed(self, index):
        if messagebox.askyesno("Delete Feed", "Are you sure you want to delete this feed?"):
            self.df = self.df.drop(index)
            self.df.to_json(self.filename, orient='records')
            self.load_feeds()

if __name__ == "__main__":
    root = tk.Tk()
    app = RSSFeedManager(root)
    root.mainloop()