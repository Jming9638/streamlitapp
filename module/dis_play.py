import streamlit as st

def summary_res(result):
    st.header("Summary:")
    col = st.columns([1,2,1,1,1])
    for i in result.columns:
        for j in result.index:
            amount = result.loc[j,i]
            if amount > 0:
                with col[0]:
                    st.write(i)
                with col[1]:
                    st.write("has to pay")
                with col[2]:
                    st.write("RM {:.2f}".format(amount))
                with col[3]:
                    st.write("to")
                with col[4]:
                    st.write(j)
