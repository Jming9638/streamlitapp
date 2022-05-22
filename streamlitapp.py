import streamlit as st
import pandas as pd
import numpy as np

from module.df2result import transformResult

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
        
        st.write('')
        st.write('Edit your value if input wrongly.')
        col2 = st.columns([1,1,1])
        with col2[0]:
            ph11 = st.empty()
            rn = ph11.text_input('Which row?')
            if rn is not None and rn != '':
                rn = int(rn)
            
        with col2[1]:
            ph22 = st.empty()
            cn = ph22.text_input('Which column?')
            
        with col2[2]:
            ph33 = st.empty()
            val = ph33.text_input('Replace with?')
        
        modify_btn = st.button("Update value")
        if modify_btn:
            try:
                df_input.loc[rn, cn] = float(val)
            except:
                df_input.loc[rn, cn] = val
        
        if df_input.shape[0] >= 1:
            st.header("Raw Data:")
            st.write(df_input)
            
            result2 = transformResult(df_input)
            st.header("Result:")
            st.write(result2.style.format("{:.2f}"))
        
        else:
            st.write("Input the parameter to see the result")
        
    else:
        st.write('Please select an option to moving forward.')


if __name__ == "__main__":
    run()
