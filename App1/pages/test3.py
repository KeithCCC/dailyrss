import streamlit as st

# Sample data list
items = ["Item 1", "Item 2", "Item 3", "Item 4"]

# Title of the app
st.title("Item Selector")

# Display the list of items in a table
st.subheader("Current Items")
st.table({"Items": items})

# Select an item from the list
selected_item = st.selectbox("Select an item to modify or remove", items)

# Display options to modify or remove the selected item
action = st.radio("What would you like to do?", ("Modify", "Remove"))

# Modify the selected item
if action == "Modify":
    new_value = st.text_input("Enter new value for the item", value=selected_item)
    if st.button("Update"):
        index = items.index(selected_item)
        items[index] = new_value
        st.success(f"Item '{selected_item}' updated to '{new_value}'")
        # Refresh the table with updated items
        st.subheader("Updated Items")
        st.table({"Items": items})

# Remove the selected item
elif action == "Remove":
    if st.button("Remove"):
        items.remove(selected_item)
        st.success(f"Item '{selected_item}' has been removed")
        # Refresh the table with updated items
        st.subheader("Updated Items")
        st.table({"Items": items})
