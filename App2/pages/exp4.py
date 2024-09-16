import streamlit as st


with st.form("my_form"):
    text_outputs = ['dogs are cute', 'dragons are real', 'birds fly']
    answer = {}
    for text_output in text_outputs:
        answer[text_output] = st.checkbox(text_output)
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(answer)