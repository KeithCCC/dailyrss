import json
import TkEasyGUI as eg
import webbrowser  # Add this import

# Load JSON data from default.json
with open('default.json', 'r') as file:
    data = json.load(file)

# Prepare the layout for displaying URLs and titles with buttons
layout = [
    [
        eg.Table(
            data=[(item['title'][:20], item['url']) for item in data],  # Create table data
            headings=["Title", "URL"],  # Define table headings
            key=[item['url'] for item in data]  # Use a list of URLs as keys for button actions
        )
    ]
]

# Create a window
with eg.Window("URL List", layout) as window:
    # Event loop
    for event, values in window.event_iter():
        if event == eg.WINDOW_CLOSED:
            break
        elif event in [item['url'] for item in data]:  # Check if a button was pressed
            webbrowser.open(event)  # Open the URL in a browser
