import streamlit as st
import pandas as pd

# Initialize a simple DataFrame
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({
        'Name': ['John', 'Jane', 'Doe'],
        'Age': [28, 34, 22]
    })

# Display the DataFrame
st.write("Current DataFrame:")
st.dataframe(st.session_state.df)

# Add a new row
st.write("Add a new row:")
new_name = st.text_input("Name")
new_age = st.number_input("Age", min_value=0, max_value=100)

if st.button("Add Row"):
    if new_name and new_age:
        new_row = pd.DataFrame({'Name': [new_name], 'Age': [new_age]})
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        # st.experimental_user()

# Remove a row
st.write("Remove a row:")
row_to_delete = st.selectbox("Select row to delete", st.session_state.df.index)

if st.button("Delete Row"):
    if row_to_delete in st.session_state.df.index:
        st.session_state.df = st.session_state.df.drop(index=row_to_delete).reset_index(drop=True)
        # st.experimental_user()

# Display the updated DataFrame
st.write("Updated DataFrame:")
st.dataframe(st.session_state.df)
