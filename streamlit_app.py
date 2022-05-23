import streamlit as st
import pandas as pd
import numpy as np

from module.df2result import transformResult
from module.input_page import input_method
from module.dis_play import summary_res
#--------------------------Set up Memory--------------------------#
if 'elem' not in st.session_state:
    st.session_state['elem'] = []


def run():
    st.set_page_config(page_title="Shared Expense Calculator")
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
            
            summary_res(result)
            end_col = st.columns([1,1,1])
            with end_col[1]:
                st.write("------End of the page------")

    elif option == 'Input': 
        input_method()
        
    else:
        st.write('Please select an option to moving forward.')


if __name__ == "__main__":
    run()
