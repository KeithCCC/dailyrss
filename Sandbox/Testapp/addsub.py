import streamlit as st
import pandas as pd

# Initialize or load the DataFrame
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]
    })

# Function to add a new row
def add_row(name, age):
    new_row = {'Name': name, 'Age': age}
    st.session_state.data = st.session_state.data.append(new_row, ignore_index=True)

# Function to delete a row by index
def delete_row(index):
    if index in st.session_state.data.index:
        st.session_state.data = st.session_state.data.drop(index).reset_index(drop=True)

st.title("DataFrame Editor")

# Display the current DataFrame with delete buttons for each row
st.subheader("Current DataFrame")

for index, row in st.session_state.data.iterrows():
    # Display row data
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    col1.write(f"Name: {row['Name']}, Age: {row['Age']}")
    
    # Add delete button for each row
    if col4.button("Delete", key=f"delete_{index}"):
        delete_row(index)
        st.success(f"Row {index} deleted!")
        if st.button("Refresh"):
            st.experimental_rerun()  # Refresh the DataFrame to reflect changes

# Section to add a new row
st.subheader("Add New Row")
name = st.text_input("Name")
age = st.number_input("Age", min_value=0, max_value=100, step=1)
if st.button("Add Row"):
    add_row(name, age)
    st.success("Row added!")
    st.experimental_rerun()  # Refresh the DataFrame

# Display the updated DataFrame after add/delete operations
st.write("Updated DataFrame:")
st.dataframe(st.session_state.data)
