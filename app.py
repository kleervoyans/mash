import streamlit as st
from utils import fetch_repo_metadata
from summariser import generate_mash

st.title('Mash')
repo_url = st.text_input('GitHub Repo URL', 'https://github.com/kleervoyans/mash')
lang = st.selectbox('Output Language', ['EN', 'DE', 'TR'])

if st.button('Generate'):
    with st.spinner('Fetching...'):
        data = fetch_repo_metadata(repo_url)
        sheet = generate_mash(data, language=lang)
    st.markdown(sheet)
    st.download_button('Download Markdown', sheet, file_name='MASH.md')