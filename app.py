import streamlit as st
from chat_app import render_chat_app
from pages.preview_data import render_table

st.set_page_config(page_title='Main')
st.title('Financial Helper')

with st.sidebar:    
    uploaded_file = st.file_uploader(
        label = 'Upload a file', 
        type=['csv'],
    )    
    if uploaded_file is not None:
        st.session_state['uploaded_file'] = uploaded_file
        st.write('Uploaded file name: ', uploaded_file.name)
        
render_table()
render_chat_app()

