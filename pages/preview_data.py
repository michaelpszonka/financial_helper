import streamlit as st
import pandas as pd

def render_table():
    if('uploaded_file' in st.session_state):             
        # # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(st.session_state['uploaded_file'])
        st.write(dataframe)            
