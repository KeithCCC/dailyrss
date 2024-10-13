import os
from tkinter import simpledialog
import pandas as pd
from tkinter import *
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

# Create the Tkinter window
root = Tk()
root.title("DataFrame Display")
root.geometry("750x600")  # Set the window width to 2400 pixels and height to 600 pixels

# Create a canvas and a scrollbar
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

# Configure the canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Set the scrollbar to the canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Define a function to handle button clicks
def on_button_click(row):
    print(f"Button clicked for row: {row}")
    webbrowser.open(row['url'])  # Open the URL in the default web browser

# Custom dialog class for multiple inputs
class MultiInputDialog(simpledialog.Dialog):
    def __init__(self, parent, title, initial_values):
        self.initial_values = initial_values
        self.result = {}
        super().__init__(parent, title)

    def body(self, frame):
        Label(frame, text="Label:").grid(row=0, column=0)
        self.label_entry = Entry(frame, width=60)  # Set width to 60 characters
        self.label_entry.grid(row=0, column=1)
        self.label_entry.insert(0, self.initial_values['label'])

        Label(frame, text="Title:").grid(row=1, column=0)
        self.title_entry = Entry(frame, width=60)  # Set width to 60 characters
        self.title_entry.grid(row=1, column=1)
        self.title_entry.insert(0, self.initial_values['title'])

        Label(frame, text="URL:").grid(row=2, column=0)
        self.url_entry = Entry(frame, width=60)  # Set width to 60 characters
        self.url_entry.grid(row=2, column=1)
        self.url_entry.insert(0, self.initial_values['url'])

    def apply(self):
        self.result['label'] = self.label_entry.get()
        self.result['title'] = self.title_entry.get()
        self.result['url'] = self.url_entry.get()

# Define a function to show the edit dialog
def show_edit_dialog(row):
    dialog = MultiInputDialog(root, "Edit Entry", {'label': row['label'], 'title': row['title'], 'url': row['url']})
    if dialog.result:
        # Truncate to 200 characters if necessary
        for key in ['label', 'title', 'url']:
            if dialog.result[key] and len(dialog.result[key]) > 200:
                dialog.result[key] = dialog.result[key][:200]

        # Update the DataFrame
        df.at[row.name, 'title'] = dialog.result['title']
        df.at[row.name, 'label'] = dialog.result['label']
        df.at[row.name, 'url'] = dialog.result['url']
        
        # Save the updated DataFrame back to JSON
        df.to_json(filename, orient='records', lines=True)

# Insert DataFrame content into the scrollable frame with buttons
for index, row in df.iterrows():
    if index >= 30:  # Limit to 30 rows
        break
    row_text = f"{row['label']} "  # Only label is bold
    label = Label(scrollable_frame, text=row_text, anchor="w", font=("Helvetica", 10, "bold"))  # Make label text bold
    label.grid(row=index, column=0, sticky="w")
    
    # Create a label for the title
    title_label = Label(scrollable_frame, text=row['title'], anchor="w", font=("Helvetica", 10))  # Set wraplength to 500 pixels
    title_label.grid(row=index, column=1, sticky="w")  # Place title in column 1
    
    # Create a label for the URL with hyperlink functionality
    url_label = Label(scrollable_frame, text=row['url'], anchor="w", fg="blue", cursor="hand2")  # Set width to 300 pixels
    url_label.grid(row=index, column=2, sticky="w")  # Place URL in column 2
    url_label.bind("<Button-1>", lambda e, url=row['url']: webbrowser.open(url))  # Open URL on click
    
    # # button_view = Button(scrollable_frame, text="View", command=lambda r=row: on_button_click(r))  # Set button width to 300 pixels
    # # button_view.grid(row=index, column=3, padx=5, pady=5)  # Adjust button column accordingly
    
    # button_edit = Button(scrollable_frame, text="Edit", command=lambda r=row: show_edit_dialog(r))  # Add edit button
    # button_edit.grid(row=index, column=4, padx=5, pady=5)  # Place edit button in column 4

# # Add a button to open default.json in Notepad
# button_open_notepad = Button(scrollable_frame, text="Open default.json", command=lambda: os.startfile("default.json"))  # Command to open Notepad with the file
# button_open_notepad.grid(row=index + 1, column=0, columnspan=5, padx=5, pady=5)  # Place button below the last row

# Create a button to edit outside the scrollable frame
# button_edit = Button(root, text="Edit", command=lambda r=row: show_edit_dialog(r))  # Add edit button
button_edit = Button(root, text="Edit file", command=lambda: os.startfile("default.json"))  # Add edit button
button_edit.pack(padx=5, pady=5)  # Place edit button outside the scrollable frame

# Run the Tkinter event loop
root.mainloop()
