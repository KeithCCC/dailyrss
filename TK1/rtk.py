import os
import pandas as pd
from tkinter import *

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

# Create a frame to hold the text and buttons
frame = Frame(root)
frame.pack(expand=YES, fill=BOTH)

# Define a function to handle button clicks
def on_button_click(row):
    print(f"Button clicked for row: {row}")

# Insert DataFrame content into the frame with buttons
for index, row in df.iterrows():
    row_text = f"{row['label']} {row['title']} {row['URL']}"
    label = Label(frame, text=row_text, anchor="w")
    label.grid(row=index, column=0, sticky="w")
    
    button = Button(frame, text="View", command=lambda r=row: on_button_click(r))
    button.grid(row=index, column=1, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
