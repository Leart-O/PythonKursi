import pandas as pd
import streamlit as st
import plotly.express as pt

book = pd.read_csv("books.csv")

st.title("Best Selling Books")
st.write("This is a program about...")

st.sidebar.header("Add a new book")

with st.sidebar.form("my_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = ("user rating", 0.5, 5, 0.0, 0.1)
    new_reviews = st.number_input("reviews", min_value=0.0, max_value=5.0, step=0.1)
    new_genre = st.text_input("Genre")
    new_price = st.number_input("Price", min_value=0.0, max_value=100.0, step=0.1)
    new_year = st.number_input("Year", min_value=1900, max_value=2024, step=1)
    submitted = st.form_submit_button("Submit")
    