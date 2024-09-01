import streamlit as st

# Sample data
items = ["Item 1", "Item 2", "Item 3"]

# Function to display items with actions
def display_items_with_actions(items):
    for item in items:
        # Create a new row with columns
        col1, col2, col3 = st.columns([2, 1, 1])  # Adjust the proportions as needed

        # Display the item in the first column
        with col1:
            st.write(item)

        # Display the first action button in the second column
        with col2:
            if st.button(f"Action 1 for {item}"):
                st.write(f"Action 1 triggered for {item}")

        # Display the second action button in the third column
        with col3:
            if st.button(f"Action 2 for {item}"):
                st.write(f"Action 2 triggered for {item}")

st.text("First Text")
st.text("Second Text")

st.text("-----------------------------")

st.markdown('<p style="margin-bottom: 5px;">First Text</p>', unsafe_allow_html=True)
st.markdown('<p style="margin-bottom: 5px;">Second Text</p>', unsafe_allow_html=True)

st.text("-----------------------------")

st.text("First Text")
st.markdown("<br>", unsafe_allow_html=True)  # Adjust spacing with an HTML break
st.text("Second Text")

st.text("-----------------------------")

# Run the function
display_items_with_actions(items)
