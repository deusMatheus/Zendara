import streamlit as st

st.title("Fichas de Zendara V 0.1")
st.write('O que deseja?')

create_sheets = st.button('Criar Fichas')
view_sheets = st.button('Visualizar Fichas')

if(create_sheets):
    st.switch_page('interface/create_sheets.py')

if(view_sheets):
    st.switch_page('interface/view_sheets.py')

