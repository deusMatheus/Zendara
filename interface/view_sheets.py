import streamlit as st
#import tailwind as tw
from classes.db_manager import db_manager as db

st.title("Visualizador de fichas")
list_of_properties = ["Nome", "Espécie","Vocação","Pontos de Experiência","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura","Condição"]

characters_list = db().select_values("*",'character_sheets')
character_names = []
for character in characters_list:
    character_names.append(character[0])

if not characters_list:
    st.write('Não há fichas cadastradas.')

else:
    tabs = st.tabs(character_names)
    for i in range(len(tabs)):
        with tabs[i]:
            for j in range(len(list_of_properties)):
                st.write(f'{list_of_properties[j]}: {characters_list[i][j]}')