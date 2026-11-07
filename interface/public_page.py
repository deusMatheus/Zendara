import streamlit as st
from classes.db_manager import db_manager as db

st.session_state['register_ability'] = False
st.session_state['edit_ability'] = False
st.session_state['register_item'] = False
st.session_state['edit_item'] = False

st.image(st.session_state['image_path'],width=500)

#st.title(f"Fichas de Zendara {st.session_state['version']}")
st.write('O que deseja?')

st.session_state['selected_character'] = False
st.session_state['character_index'] = None

#st.write(db().full_database_path)

columns = st.columns(2)

with columns[0]:
    create_sheets = st.button('Criar Fichas')

with columns[1]:
    view_sheets = st.button('Visualizar Fichas')

if(create_sheets):
    st.switch_page('interface/create_sheets.py')

if(view_sheets):
    st.switch_page('interface/view_sheets.py')

