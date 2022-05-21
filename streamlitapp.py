import streamlit as st
import pandas as pd
import numpy as np

#--------------------------Set up Memory--------------------------#
if 'elem' not in st.session_state:
    st.session_state['elem'] = []
    
if 'input_row' not in st.session_state:
    st.session_state['input_row'] = 1

#--------------------------Function--------------------------#
def split_comma(txt):
    l = txt.replace(' ', '').split(',')
    return l

def count_ppl(ppl):
    c = len(ppl)
    return c

#--------------------------Function--------------------------#
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
            
            df['for'] = df['for'].apply(split_comma)
            df['ppl'] = df['for'].apply(count_ppl)
            df['divided_amount'] = df['amount']/df['ppl']
            df_ex = df.explode('for', ignore_index=True)

            corrected_list = []
            for i in range(df_ex.shape[0]):
                if df_ex['paid'][i] == df_ex['for'][i]:
                    corrected_list.append(0)
                else:
                    corrected_list.append(df_ex['divided_amount'][i])

            df_ex['divided_amount'] = corrected_list
            df_pivot = pd.pivot_table(df_ex, index='paid', columns='for', values='divided_amount', aggfunc='sum', fill_value=0)
            
            full_list = []
            for i in df_pivot.index:
                row_result = []
                for j in df_pivot.columns:
                    if i==j:
                        row_result.append(0)
                    else:
                        try:
                            num = df_pivot.loc[i,j] - df_pivot.loc[j,i]
                            row_result.append(num)
                        except:
                            row_result.append(df_pivot.loc[i,j])
                full_list.append(row_result)

            result = pd.DataFrame(full_list, columns=df_pivot.columns, index=df_pivot.index)
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
            
            df_input['for'] = df_input['for'].apply(split_comma)
            df_input['ppl'] = df_input['for'].apply(count_ppl)
            df_input['divided_amount'] = df_input['amount']/df_input['ppl']
            df_ex = df_input.explode('for', ignore_index=True)

            corrected_list = []
            for i in range(df_ex.shape[0]):
                if df_ex['paid'][i] == df_ex['for'][i]:
                    corrected_list.append(0)
                else:
                    corrected_list.append(df_ex['divided_amount'][i])

            df_ex['divided_amount'] = corrected_list
            df_pivot = pd.pivot_table(df_ex, index='paid', columns='for', values='divided_amount', aggfunc='sum', fill_value=0)
            
            full_list = []
            for i in df_pivot.index:
                row_result = []
                for j in df_pivot.columns:
                    if i==j:
                        row_result.append(0)
                    else:
                        try:
                            num = df_pivot.loc[i,j] - df_pivot.loc[j,i]
                            row_result.append(num)
                        except:
                            row_result.append(df_pivot.loc[i,j])
                full_list.append(row_result)

            result = pd.DataFrame(full_list, columns=df_pivot.columns, index=df_pivot.index)
            st.header("Result:")
            st.write(result.style.format("{:.2f}"))
        
        else:
            st.write("Input the parameter to see the result")
        
    else:
        st.write('Please select an option to moving forward.')


if __name__ == "__main__":
    run()
    
