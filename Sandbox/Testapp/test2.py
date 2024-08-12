import streamlit as st
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame as a static table in a Streamlit app
st.table(df)
