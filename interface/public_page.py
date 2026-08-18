import streamlit as st

st.session_state['register_ability'] = False

st.title(f"Fichas de Zendara {st.session_state['version']}")
st.write('O que deseja?')

create_sheets = st.button('Criar Fichas')
#create_sheets = ''
view_sheets = st.button('Visualizar Fichas')

if(create_sheets):
    st.switch_page('interface/create_sheets.py')

if(view_sheets):
    st.switch_page('interface/view_sheets.py')

