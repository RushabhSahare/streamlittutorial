import streamlit as st
import requests

st.title('st.secrets')

api_key=st.secrets["my_api"]["key"]
base_url=st.secrets["my_api"]["base_url"]

headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(base_url, headers=headers)

st.write("API call made")