import TkEasyGUI as eg
import json
import pandas as pd
import webbrowser  # Add this import
import os

# Load JSON data from file with UTF-8 encoding
filename = "default.json"
if os.path.exists(filename):
    try:
        df = pd.read_json(filename)
        # Reorder the columns
        df = df[['label', 'title', 'url']]
    except Exception as e:
        print(e)

layout = []

for index, row in df.iterrows():
    # row_text = f" <strong>{{{row['label']}</strong> {row['title']}"
    row_label = f" {row['label']}"
    row_title = f" {row['title']}"
    row_url= f" {row['url']}"
    layout.append([eg.Text(row_label, color="green"),
                   eg.Text(row_title, color="black"),
                   eg.Text(row_url, color="blue", enable_events=True)])

# Create the window
window = eg.Window('Clickable Items', layout)

# Event loop
while True:
    event, values = window.read()
    if event == eg.WIN_CLOSED:
        break
    # Check if a text item was clicked
    print("event:", event)
    clean_list = event.strip('-').replace("'", '"')
    webbrowser.open(event)
    # eg.popup(f'Item: {clean_list}')  # Display the item data

window.close()