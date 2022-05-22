import streamlit as st
import pandas as pd
import numpy as np

from module.df2result import transformResult

#--------------------------Set up Memory--------------------------#
if 'elem' not in st.session_state:
    st.session_state['elem'] = []
    
if 'input_row' not in st.session_state:
    st.session_state['input_row'] = 1

def run():
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
        number_of_row = st.session_state['input_row']
        
        col = st.columns([1, 1, 1, 1])
        
        with col[0]:
            ph1 = st.empty()
            paid = ph1.text_input('Who paid?')
            
        with col[1]:
            ph2 = st.empty()
            amount = ph2.text_input('Amount')
            
        with col[2]:
            ph3 = st.empty()
            for_ = ph3.text_input('Paid for who?')
            
        with col[3]:
            ph4 = st.empty()
            item = ph4.text_input('Item/Activity')
        
        input_btn = st.button("Add")
        if input_btn:
            st.session_state['elem'].append([paid, float(amount), for_, item])
            
        input_list = st.session_state['elem']
        df_input = pd.DataFrame(input_list, columns=['paid', 'amount', 'for', 'item'])
        
        if df_input.shape[0] >= 1:
            st.header("Raw Data:")
            st.write(df_input)
            
            result2 = result = transformResult(df_input)
            st.header("Result:")
            st.write(result2.style.format("{:.2f}"))
        
        else:
            st.write("Input the parameter to see the result")
        
    else:
        st.write('Please select an option to moving forward.')


if __name__ == "__main__":
    run()
