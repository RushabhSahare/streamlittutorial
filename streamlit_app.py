import streamlit as st

st.header('st.button')

if st.button('Hello World!'):
    st.write('Why Hello There')
else:
    st.write('Goodbye')