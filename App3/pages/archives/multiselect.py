import streamlit as st

# Sample list of items
items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grapes']

# Dictionary to store checkbox states
selected_items = {}

# Display checkboxes for each item in the list
st.write("Select the fruits you like:")
for item in items:
    selected_items[item] = st.checkbox(item)

# Button to perform an action
if st.button('Submit'):
    # Get the list of selected items
    selected = [item for item, is_checked in selected_items.items() if is_checked]
    
    if selected:
        # Display the selected items
        st.write(f"You selected: {', '.join(selected)}")
        
        # Example action: Display the number of selected items
        st.write(f"Number of fruits selected: {len(selected)}")

        # Example action: Perform some processing on selected items
        st.write("Processing selected items...")
        processed_items = [item.upper() for item in selected]
        st.write(f"Processed items: {', '.join(processed_items)}")
    else:
        st.write("Please select at least one fruit.")
