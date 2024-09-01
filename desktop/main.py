
import json
import tkinter as tk
from tkinter import messagebox

# Function to load JSON data from a file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return []
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Invalid JSON format.")
        return []

# Function to save JSON data to a file
def save_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to remove the selected item
def remove_selected():
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        del data[selected_index[0]]  # Remove from the list
        listbox.delete(selected_index)  # Remove from the listbox
        save_json_file(file_path, data)  # Save changes to the JSON file
        messagebox.showinfo("Success", f"Removed: {selected_item}")
    else:
        messagebox.showwarning("Warning", "No item selected.")

# Set up the GUI window
def create_gui(data):
    global listbox
    root = tk.Tk()
    root.title("JSON Viewer and Editor")

    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
    listbox.pack(pady=10)

    # Populate the listbox with data
    for item in data:
        listbox.insert(tk.END, item)

    remove_button = tk.Button(root, text="Remove Selected", command=remove_selected)
    remove_button.pack(pady=5)

    root.mainloop()

# Load JSON data from a file
file_path = 'data.json'  # Replace with your JSON file path
data = load_json_file(file_path)

# Start the GUI if data is loaded
if data:
    create_gui(data)
