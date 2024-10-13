import os
import PySimpleGUI as sg
import pandas as pd
import webbrowser  # Add this import

# Load the DataFrame
filename = "default.json"
if os.path.exists(filename):
    try:
        df = pd.read_json(filename)
        # Reorder the columns
        df = df[['label', 'title', 'url']]
    except Exception as e:
        print(e)

layout = []

def create_row(row):
    """Creates a row for the GUI layout."""
    row_label = f" {row['label']}"
    row_title = f" {row['title']}"
    row_url = f" {row['url']}"
    return [sg.Text(row_label), sg.Text(row_title), sg.Text(row_url, enable_events=True)]

for index, row in df.iterrows():
    layout.append(create_row(row))  # Use the create_row function

window = sg.Window("Hello App", layout)

def handle_event(event, values):
    """Handles the events from the window."""
    print("event:", event)
    print("values:", values)    
    print("event[:5]", event[:5])
    if event.startswith("http"):
        print("opening:", event)
        webbrowser.open(event, new=2)  # Open the URL in a new tab
    return event 

while True:
    event, values = window.read()
    if handle_event(event, values):  # Pass values to handle_event
        break

window.close()
