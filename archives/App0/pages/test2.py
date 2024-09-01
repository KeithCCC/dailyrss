import streamlit as st

# First list
first_list = ['First Item 1', 'First Item 2', 'First Item 3']

# Second list (to be displayed after button press)
second_list = ['Second Item 1', 'Second Item 2', 'Second Item 3']

# Initialize session state to track if the button has been clicked
if 'show_second_list' not in st.session_state:
    st.session_state.show_second_list = False

# Display the first list
st.write("### First List")
for item in first_list:
    st.write(item)

# Button to show the second list
if st.button("Show Second List"):
    st.session_state.show_second_list = True

# Display the second list if the button has been pressed
if st.session_state.show_second_list:
    st.write("### Second List")
    for item in second_list:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(item)
        with col2:
            if st.button(f"Click Me ({item})", key=item):
                st.write(f'You clicked on {item}')

