import time
import streamlit as st
from classes.db_manager import db_manager as db

st.title("Criador de fichas")
list_of_properties = ["Nome do personagem", "Espécie","Vocação","Pontos de Experiência","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura"]
list_of_inputs = []

with st.form("form_char_sheet_creation"):
    for property in list_of_properties:
        char_input = st.text_input(property)
        list_of_inputs.append(char_input)
    create_sheet_button = st.form_submit_button('Criar ficha')

    if(create_sheet_button):
        try:
            db().insert_values('character_sheets',[f'("{list_of_inputs[0]}","{list_of_inputs[1]}","{list_of_inputs[2]}","{list_of_inputs[3]}","{list_of_inputs[4]}","{list_of_inputs[5]}","{list_of_inputs[6]}","{list_of_inputs[7]}","{list_of_inputs[8]}","{list_of_inputs[9]}","{list_of_inputs[10]}","{list_of_inputs[11]}","{list_of_inputs[12]}","{list_of_inputs[13]}","none")'])
            st.warning('Sucesso na criação da ficha! Aguarde...')
            time.sleep(3)
#        st.switch_page('public_page.py')

        except:
            st.warning('Aconteceu um erro')
            time.sleep(3)
        st.switch_page('interface/public_page.py')

