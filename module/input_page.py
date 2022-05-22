import streamlit as st
import pandas as pd

from .df2result import transformResult, to_excel
from .dis_play import summary_res

def input_method():
    col = st.columns([1, 1, 2, 1])
        
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
    
    btn_col = st.columns([0.6,0.6,2,1,1])
    with btn_col[0]:
        input_btn = st.button("Add")
        if input_btn:
            st.session_state['elem'].append([paid, float(amount), for_, item])
            
    with btn_col[1]:
        delete_btn = st.button("Delete")
        if delete_btn:
            try:
                del st.session_state['elem'][-1]
            except:
                with btn_col[2]:
                    st.write("")
                    st.write("No more rows.")
        
    input_list = st.session_state['elem']
    
    if len(input_list) >= 1:
    
        st.write('')
        st.write('Edit your value if input wrongly.')
        col2 = st.columns([1,1,1])
        with col2[0]:
            rn = st.selectbox('Which column?', range(len(input_list)))
            if rn is not None and rn != '':
                try:
                    rn = int(rn)
                except:
                    rn = 0
            
        with col2[1]:
            cn = st.selectbox('Which column?', ('-Select column-', 'paid', 'amount', 'for', 'item'))
            if cn == 'paid':
                cname = 0
            elif cn == 'amount':
                cname = 1
            elif cn == 'for':
                cname = 2
            elif cn == 'item':
                cname = 3
            
        with col2[2]:
            ph33 = st.empty()
            val = ph33.text_input('Replace with?')
        
        modify_btn = st.button("Update value")
        if modify_btn and cn != '-Select column-':
            try:
                st.session_state['elem'][rn][cname] = float(val)
            except:
                st.session_state['elem'][rn][cname] = val
        
        df_input = pd.DataFrame(input_list, columns=['paid', 'amount', 'for', 'item'])
        st.header("Raw Data:")
        st.write(df_input)
        
        df_xlsx = to_excel(df_input)
        st.download_button(label='Download as Excel Workbook', 
                            data=df_xlsx, 
                            file_name= 'raw_data.xlsx')
        
        result2 = transformResult(df_input)
        st.header("Result:")
        st.write(result2.style.format("{:.2f}"))
        
        summary_res(result2)
    
    else:
        st.write("Input the parameter to see the result")
