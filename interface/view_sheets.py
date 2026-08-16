import streamlit as st
#import tailwind as tw
from classes.db_manager import db_manager as db

st.title("Visualizador de fichas")
list_of_properties = ["Nome", "Espécie","Vocação","Pontos de Experiência","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura","Condição"]

#characters_list = db().select_values("*",'character_sheets')
characters_list = st.session_state['characters_list']
#print(characters_list)
character_names = []
for character in characters_list:
    character_names.append(character[0])

if not characters_list:
    st.write('Não há fichas cadastradas.')

else:
    character_selected = st.selectbox('Selecione um personagem',character_names,placeholder='Selecione um personagem',index=None)

    if(not character_selected):
        st.write('Nenhum personagem selecionado')

    elif(character_selected in character_names):
        character_index = character_names.index(character_selected)
        for j in range(len(list_of_properties)):
            st.write(f'{list_of_properties[j]}: {characters_list[character_index][j]}')
        skill_categories = characters_list[character_index][-1].split(",")

        st.title('Habilidades')

        tabs = st.tabs(skill_categories)
        for i in range(len(skill_categories)):
            with tabs[i]:
                st.write(f'Skill de {skill_categories[i]}')

    else:
        st.write('Ocorreu um problema, contate o administrador do sistema')

#    tabs = st.tabs(character_names)
#    for i in range(len(tabs)):
#        with tabs[i]:
#            for j in range(len(list_of_properties)):
#                st.write(f'{list_of_properties[j]}: {characters_list[i][j]}')
#            skill_categories = characters_list[i][-1].split(",")
#            for category in skill_categories:
#                st.write(category)