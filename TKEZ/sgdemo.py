import PySimpleGUI as sg
import json

# Load JSON data from file with UTF-8 encoding
with open('default.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a layout with clickable text for each item
layout = [[sg.Text(item, key=f'-{item}-', enable_events=True)] for item in data]

# Create the window
window = sg.Window('Clickable Items', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # Check if a text item was clicked
    print("event:", event)
    if event.startswith('-'):
        item_name = event[1:]  # Remove the '-' prefix
        item_data = data[item_name]  # Get the corresponding data
        sg.popup(f'Item: {item_name}\nData: {item_data}')  # Display the item data

window.close()
