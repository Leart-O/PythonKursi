import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("Column 1")
    st.write("Random stuff")

with col2:
    st.header("Column 2")
    st.write("Random stuff")

with col3:
    st.header("Column 3")
    st.write("Random stuff")

with col4:
    st.header("Column 4")
    st.write("Random stuff")

with col5:
    st.header("Column 5")
    st.write("Random stuff")

with st.container():
    st.header("Container")
    st.subheader("This is inside a container")

tab1, tab2, tab3 = st.tabs(["News", "Sport", "Economy"])

with tab1:
    st.header("News")
    st.write("News content")

with tab2:
    st.header("Sport")
    st.write("Sport content")

with tab3:
    st.header("Economy")
    st.write("Economy content")