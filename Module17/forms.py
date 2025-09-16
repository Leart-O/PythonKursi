import streamlit as st

with st.form("my_form", clear_on_submit=True):
    name = st.text_input("Name")
    age = st.slider("Age", min_value=0, max_value=100)
    email = st.text_input("Email")
    bio = st.text_area("Bio")
    terms = st.checkbox("I agree to the terms and ...")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"DESC: {bio}")
    
    if terms:
        st.write("You agreed to the terms")
    else:
        st.write("You didn't agree to the terms")