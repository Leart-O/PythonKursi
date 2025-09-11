import streamlit as st

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operator = st.text_input("Enter operator (+, -, *, /):")

if st.button("Calculate"):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
            result = num1 / num2

    
    st.write("Result:", result) 
    