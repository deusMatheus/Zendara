import streamlit as st
from time import sleep
from classes.db_manager import db_manager as db

def registerAbility(abilityName, abilityDesc, abilityCateg, characterName):
    st.session_state['register_form'] = True
    if (abilityName != '' and abilityDesc != '' and abilityCateg != '' and st.session_state['register_form']):
        try:
            db().create_ability(abilityName, abilityDesc, abilityCateg, characterName)
            st.write('Cadastro de habilidade concluído!')
            st.toast('Cadastro de habilidade concluído!')
            st.toast('Cadastro de habilidade concluído!')
        except:
            st.toast('Algo de errado aconteceu.')
    sleep(1)
    st.session_state['register_ability'] = False
    st.switch_page('interface/public_page.py')

if(st.session_state['register_ability']):
    st.title(f'Registrar habilidade para {st.session_state['character_name']}')
#            st.session_state['register_pressed'] = True
    with st.form('register_ability_form'):
        character_name = st.session_state['character_name'] 
        ability_name = st.text_input('Nome da habilidade', placeholder='Nome da habilidade', key='ability_name')
        ability_desc = st.text_area('Descrição da habilidade', placeholder='Descrição da habilidade', key='ability_desc')
        ability_categ = st.selectbox('Selecione uma categoria', st.session_state['abilities_categories_by_character'], placeholder='Selecione uma categoria', index=None, key='ability_categ')
        st.session_state['register_ability'] = True 
        if st.form_submit_button(label='Registrar'):
            registerAbility(ability_name, ability_desc, ability_categ, character_name)

else:
    st.title("Ops!")
    st.write('Para registrar uma habilidade, primeiro selecione um personagem no **Visualizador de fichas** e clique no botão **Cadastrar nova habilidade**.')

