from time import sleep
import streamlit as st
#import tailwind as tw
from classes.db_manager import db_manager as db

if 'characters_list' in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

if 'register_form' not in st.session_state:
    st.session_state['register_form'] = False

st.session_state['register_ability'] = False

#def registerAbility():
#    abilityName = st.session_state['ability_name']
#    abilityDesc = st.session_state['ability_desc']
#    abilityCateg = st.session_state['ability_categ']
#    characterName = st.session_state['char_name']
#    print('HEY!')
#    st.session_state['register_form'] = True
#    if (abilityName != '' and abilityDesc != '' and abilityCateg != '' and st.session_state['register_form']):
#        print('HHHHHEEEEYYYYYY!')
#        try:
#            db().create_ability(abilityName, abilityDesc, abilityCateg, characterName)
#            st.write('Cadastro de habilidade concluído!')
#            st.toast('Cadastro de habilidade concluído!')
#            st.toast('Cadastro de habilidade concluído!')
#        except:
#            st.toast('Algo de errado aconteceu.')
#    sleep(1)
#    st.switch_page('interface/public_page.py')
#    st.session_state['register_pressed'] = False
#    st.session_state['register_form'] = False
#    st.session_state['register_form'] = False
#    st.session_state['register_ability'] = False
#
st.title("Visualizador de fichas")
list_of_properties = ["Nome", "Espécie","Vocação","Pontos de Experiência","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura","Condição"]

#characters_list = db().select_values("*",'character_sheets')
characters_list = st.session_state['characters_list']
#print(characters_list)
character_names = []
for character in characters_list:
    character_names.append(character[0])

if not characters_list:
    st.write('Não há personagens cadastrados.')

else:
    character_selected = st.selectbox('Selecione um personagem',character_names,placeholder='Selecione um personagem',index=None)

    if(not character_selected):
        st.write('Nenhum personagem selecionado')

    elif(character_selected in character_names):
        character_index = character_names.index(character_selected)
        for j in range(len(list_of_properties)):
            st.write(f'{list_of_properties[j]}: {characters_list[character_index][j]}')
#        skill_categories = characters_list[character_index][-1].split(",")

        st.title('Habilidades')

        abilities_by_character = db().list_abilities_by_character(characters_list[character_index][0])
        abilities_categories_by_character = db().list_abilities_categories_by_character(characters_list[character_index][0])
        abilities_categories_by_character_formated = []

#        print('TESTE 1\n')
#        print(abilities_by_character)
#        print('TESTE 2\n')
#        print(abilities_categories_by_character)

        list_of_tabs = []
        for category in abilities_categories_by_character:
            list_of_tabs.append(category[0])
            abilities_categories_by_character_formated.append(category[0])

        register_ability = st.button('Cadastrar nova habilidade')

        st.session_state['character_name'] = characters_list[character_index][0]
        st.session_state['abilities_categories_by_character'] = abilities_categories_by_character_formated
        if(register_ability):
            st.session_state['register_ability'] = True
            st.switch_page('interface/register_ability.py')
#            st.session_state['register_ability'] = True
#            if(st.session_state['register_ability']):
#    #            st.session_state['register_pressed'] = True
#                if st.button('TESTE'):
#                    print(hey!)
#                with st.form('register_ability_form'):
#                    print('yoooo')
#                    st.session_state['char_name'] = characters_list[character_index][0]
#                    ability_name = st.text_input('Nome da habilidade', placeholder='Nome da habilidade', key='ability_name')
#                    ability_desc = st.text_input('Descrição da habilidade', placeholder='Descrição da habilidade', key='ability_desc')
#                    ability_categ = st.selectbox('Selecione uma categoria', abilities_categories_by_character_formated, placeholder='Selecione uma categoria', index=None, key='ability_categ')
#                    st.session_state['register_ability'] = True 
#                    if st.form_submit_button(label='Registrar'):
##                    if (register_button):
#                        print('HE2Y!')
#                        st.session_state['register_form'] = True
#                        registerAbility()

#            if(ability_name):
#                st.write(ability_name)
#            finish_register = st.button('Finalizar cadastro')

#            if(finish_register):
#                if(not ability_name or not ability_desc or ability_categ):
#                    st.warning('EXISTEM CAMPOS EM BRANCO!', icon=':warning:')
#                else:
#                    st.write(ability_name)
#                    st.write(ability_desc)
#                    st.write(ability_categ)
#                    st.session_state['register_pressed'] = False

#        for ability in abilities_by_character:
#            if(ability['categoria'] not in list_of_tabs):
#                list_of_tabs.append(ability['categoria'])

        tabs = st.tabs(list_of_tabs)
        for i in range(len(tabs)):
            with tabs[i]:
                if not abilities_by_character:
                    st.write('Não há habilidade cadastrada para este personagem.')
                else:
                    for ability in abilities_by_character:
#                        print('TESTE')
#                        print(ability['habilidade'])
#                        print(ability['categoria'])
                        if list_of_tabs[i] == ability['categoria']:
                            st.subheader(ability['habilidade']['nome'])
                            st.write(ability['habilidade']['desc'])
                            st.divider()
                        elif list_of_tabs[i] != ability['categoria'] and not ability['categoria']:
                            st.write('Não há habilidade cadastrada nesta categoria.')

#        st.write(abilities_by_character)

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