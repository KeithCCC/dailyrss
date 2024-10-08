import json
import TkEasyGUI as eg
import webbrowser  # Add this import

# Load JSON data from default.json
with open('default.json', 'r') as file:
    data = json.load(file)

# Prepare the layout for displaying URLs and titles with buttons
layout = [
    [
        eg.Text(f"{item['title']}: {item['url']}", size=(80, 1), font=("Arial", 12)),
        eg.Button("Open", key=item['url'])  # Add a button for each URL
    ] for item in data
]

# Create a window
with eg.Window("URL List", layout) as window:
    # Event loop
    for event, values in window.event_iter():
        if event == eg.WINDOW_CLOSED:
            break
        elif event in [item['url'] for item in data]:  # Check if a button was pressed
            webbrowser.open(event)  # Open the URL in a browser
