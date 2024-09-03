import streamlit as st

# Define a list of items, each with multiple properties
items = [
    {"name": "Item 1", "property1": "Value 1", "property2": "Value 2"},
    {"name": "Item 2", "property1": "Value 3", "property2": "Value 4"},
    {"name": "Item 3", "property1": "Value 5", "property2": "Value 6"},
]

# Create a dictionary to store the checkbox states
checkbox_states = {}

# Loop through the items and create a checkbox for each with a unique key
for i, item in enumerate(items):
    key = f"checkbox_{i}"
    checkbox_states[item["name"]] = st.checkbox(f"{item['name']} - {item['property1']}, {item['property2']}", key=key)

# Display the selected items
selected_items = [item for item in items if checkbox_states[item["name"]]]
st.write("Selected items:", selected_items)
