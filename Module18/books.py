import streamlit as st
import pandas as pd

books_df = pd.read_csv("bestsellers_with_categories_2022_03_27.csv")
st.title('Best selling books')
st.write("This app shows a list of best selling books from 2009-2022")

st.subheader('Summary Statistics')

total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)