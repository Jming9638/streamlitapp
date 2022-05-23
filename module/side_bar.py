import streamlit as st
import random
import string

if 'row_count' not in st.session_state:
    st.session_state['row_count'] = 0
if 'name_list' not in st.session_state:
    st.session_state['name_list'] = []


uni_name = []
def sidebar():
    with st.sidebar:
        st.title("Manage member")
        row_btn = st.button("Add Member")
        if row_btn:
            st.session_state['row_count'] += 1
            
        for i in range(st.session_state['row_count']):
            st.session_state['name_list'].append(st.text_input("Name", key=i))
            
        for name in st.session_state['name_list']:
            if name not in uni_name and name != "":
                uni_name.append(name)
        st.session_state['name_list'] = uni_name
        name_list = st.session_state['name_list']
             
    return name_list
