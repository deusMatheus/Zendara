import time
import streamlit as st
from classes.db_manager import db_manager as db

st.session_state['register_ability'] = False
st.session_state['edit_ability'] = False
st.session_state['register_item'] = False
st.session_state['edit_item'] = False
st.session_state['selected_character'] = False
st.session_state['character_index'] = None

st.title("Criador de fichas")

with st.form("form_char_sheet_creation"):
    char_name = st.text_input('Nome do personagem',placeholder='Nome do Personagem')
    char_spec = st.text_input('Espécie',placeholder='Espécie')
    char_job = st.text_input('Vocação',placeholder='Vocação')
    char_str = st.number_input('Força',0,step=1)
    char_agi = st.number_input('Agilidade',0,step=1)
    char_log = st.number_input('Raciocínio',0,step=1)
    char_spr = st.number_input('Espiritualidade',0,step=1)
    char_mov = st.number_input('Movimento',0,step=1)
    create_sheet_button = st.form_submit_button('Criar ficha')

    if(create_sheet_button):
        if(char_name != '' and
           char_spec != '' and
           char_job != ''):
            try:
                db().create_character(char_name,char_spec,char_job,"20",char_str,char_agi,char_log,char_spr,char_mov)
                st.warning('Sucesso na criação da ficha! Aguarde...')
                time.sleep(3)

            except:
                st.warning('Aconteceu um erro')
                time.sleep(3)
            st.switch_page('interface/view_sheets.py')
        else:
            st.warning('Não foi possível criar a ficha pois há campos em branco.')

