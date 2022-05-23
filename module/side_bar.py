import streamlit as st

uni_name = []
def sidebar():
    with st.sidebar:
        if 'count' not in st.session_state:
            st.session_state['count'] = 1
        if 'name_list' not in st.session_state:
            st.session_state['name_list'] = []
        else:
            st.session_state['name_list'] = []
        
        st.title("Manage Member")
            
        for i in range(st.session_state['count']):
            st.session_state['name_list'].append(st.text_input("Name", key=i))
            
        for name in st.session_state['name_list']:
            if name not in uni_name and name != "":
                uni_name.append(name)
        st.session_state['name_list'] = uni_name
        name_list = st.session_state['name_list']
        
        side_col = st.columns([1,1])
        with side_col[0]:
            row_btn = st.button("Add Member")
            if row_btn:
                st.session_state['count'] += 1
                st.experimental_rerun()
        
        if len(st.session_state['name_list'])>=1:
            with side_col[1]:
                del_btn = st.button("Delete Member")
                if del_btn:
                    del st.session_state['name_list'][-1]
                    st.session_state['count'] -= 1
                    st.experimental_rerun()
         
    return name_list
