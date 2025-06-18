import streamlit as st

st.title('st.secrets')

st.write(st.secrets["my_api"]["key"])
st.write(st.secrets["my_api"]["base_url"])

headers = {"Authorization": f"Bearer {key}"}
response = requests.get(base_url, headers=headers)

st.write("API call made")