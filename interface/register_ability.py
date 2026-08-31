import streamlit as st
from time import sleep
from classes.db_manager import db_manager as db

st.session_state['register_item'] = False
st.session_state['edit_item'] = False

def registerAbility(abilityName, abilityDesc, abilityCateg, characterName):
    st.session_state['register_form'] = True
    if (abilityName != '' and abilityDesc != '' and abilityCateg != '' and st.session_state['register_form']):
        try:
            db().create_ability(abilityName, abilityDesc, abilityCateg, characterName)
            st.write('Cadastro de conhecimento concluído!')
            st.toast('Cadastro de conhecimento concluído!')
            st.toast('Cadastro de conhecimento concluído!')
        except:
            st.toast('Algo de errado aconteceu.')
    sleep(1)
    st.session_state['register_ability'] = False
    st.switch_page('interface/view_sheets.py')

def editAbility(oldAbilityname, newAbilityName, newAbilityDesc, newAbilityCateg, characterName):
    if(oldAbilityname != '' and newAbilityName != '' and newAbilityDesc != '' and newAbilityCateg != '' and characterName !=''):
        try:
            db().update_ability(oldAbilityname, newAbilityName, newAbilityDesc, newAbilityCateg, characterName)
            st.write('Edição de conhecimento concluído!')
            st.toast('Edição de conhecimento concluído!')
            st.toast('Edição de conhecimento concluído!')
        except:
            st.toast('Algo de errado aconteceu.')
    sleep(1)
    st.session_state['edit_ability'] = False
    st.switch_page('interface/view_sheets.py')

if(st.session_state['register_ability']):
    st.title(f'Registrar Conhecimento para {st.session_state['character_name']}')
#            st.session_state['register_pressed'] = True
    with st.form('register_ability_form'):
        character_name = st.session_state['character_name'] 
        ability_name = st.text_input('Nome do Conhecimento', placeholder='Nome do Conhecimento', key='ability_name')
        ability_desc = st.text_area('Descrição do Conhecimento', placeholder='Descrição do Conhecimento', key='ability_desc')
        ability_categ = st.selectbox('Selecione uma categoria', st.session_state['abilities_categories_by_character'], placeholder='Selecione uma categoria', index=None, key='ability_categ')
        st.session_state['register_ability'] = True 
        if st.form_submit_button(label='Registrar'):
            registerAbility(ability_name, ability_desc, ability_categ, character_name)

elif(st.session_state['edit_ability']):
    character_name = st.session_state['character_name']
    edit_ability_name = ''
    edit_ability_desc = ''
    edit_ability_categ = ''

    st.title(f'Selecione um Conhecimento de {character_name} para editar')
    ability_list_names = []
    for ability in st.session_state['abilities_by_character']:
        ability_list_names.append(ability['habilidade']['nome'])
    selected_ability = st.selectbox('Selecione um conhecimento',ability_list_names,placeholder='Selecione um conhecimento', index=None)

    if(not selected_ability):
        st.write('Nenhum conhecimento selecionado')
    else:
        for ability in st.session_state['abilities_by_character']:
            if(selected_ability in ability['habilidade']['nome']):
                edit_ability_name = ability['habilidade']['nome']
                edit_ability_desc = ability['habilidade']['desc']
                edit_ability_categ = ability['categoria']
        with st.form('edit_ability_form'):
            new_ability_name = st.text_input('Nome do conhecimento', value=edit_ability_name, placeholder='Nome do conhecimento')
            new_ability_desc = st.text_area('Descrição do conhecimento',value=edit_ability_desc, placeholder='Descrição do conhecimento')
            new_ability_categ = st.selectbox('Categoria do conhecimento',st.session_state['abilities_categories_by_character'],index=st.session_state['abilities_categories_by_character'].index(edit_ability_categ))
            if st.form_submit_button(label='Editar habilidade'):
                st.session_state['edit_ability'] = True
                editAbility(edit_ability_name, new_ability_name, new_ability_desc, new_ability_categ, character_name)
else:
    st.title("Ops!")
    st.write('Para registrar um conhecimento, primeiro selecione um personagem no **Visualizador de fichas** e clique no botão **Cadastrar novo Conhecimento**.')

