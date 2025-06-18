import streamlit as st

st.title('st.secrets')

api_key=st.write(st.secrets["my_api"]["key"])
base_url=st.write(st.secrets["my_api"]["base_url"])

headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(base_url, headers=headers)

st.write("API call made")