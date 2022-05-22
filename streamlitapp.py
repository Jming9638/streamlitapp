import streamlit as st
import pandas as pd
import numpy as np

from module.df2result import transformResult
from module.input_page import input_method
#--------------------------Set up Memory--------------------------#
if 'elem' not in st.session_state:
    st.session_state['elem'] = []


def run():
    st.title("Shared Expenses Calculator")
    
    option = st.selectbox(
        'Upload file or input manually?',
        ('-Select option-', 'Upload', 'Input'))

    if option == 'Upload':
        uploaded_file = st.file_uploader("Choose a .xlsx/.csv file", accept_multiple_files=False)
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
            except:
                df = pd.read_excel(uploaded_file)
            
            st.header("Raw Data:")
            st.write(df)
            
            result = transformResult(df)
            st.header("Result:")
            st.write(result.style.format("{:.2f}"))

    elif option == 'Input': 
        input_method()
        
    else:
        st.write('Please select an option to moving forward.')


if __name__ == "__main__":
    run()
