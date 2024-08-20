import streamlit as st
import pandas as pd

# Sample DataFrame
if 'df' not in st.session_state:
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Occupation': ['Engineer', 'Doctor', 'Artist']
    }
    st.session_state.df = pd.DataFrame(data)


# df = pd.DataFrame(data)

st.write("### DataFrame Row by Row")

# Iterate through each row in the DataFrame
for index, row in st.session_state.df.iterrows():
    # Display each row as a list
    st.write(f"Row {index + 1}: {row.tolist()}")

    # Add a button for each row
    if st.button(f"Process Row {index + 1}", key=f"button_{index}"):
        st.write(f"Processing row {index + 1}: {row['Name']}, {row['Age']}, {row['Occupation']}")
        new_row = pd.DataFrame({'Name': [row['Name']], 'Age': [row['Age']], 'Occupation': [row['Occupation']]})
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
        
st.dataframe(st.session_state.df)
# Add any additional action here when a button is clicked.
