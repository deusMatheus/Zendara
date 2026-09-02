from time import sleep
from math import floor
import streamlit as st
#import tailwind as tw
from classes.db_manager import db_manager as db

if 'i' not in st.session_state:
    st.session_state['i'] = 0

#input_number_pixels = 135

if 'characters_list' in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

if 'register_form' not in st.session_state:
    st.session_state['register_form'] = False

if 'disabled_button' not in st.session_state:
    st.session_state['disabled_button'] = True

st.session_state['register_ability'] = False
st.session_state['edit_ability'] = False
st.session_state['register_item'] = False
st.session_state['edit_item'] = False

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
st.subheader("Visualizador de fichas")
list_of_properties = ["Nome", "Espécie","Vocação","Pontos de Experiência","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento", "Defesa"]

#characters_list = db().select_values("*",'character_sheets')
characters_list = st.session_state['characters_list']
#print(characters_list)
character_names = []
for character in characters_list:
    character_names.append(character[0])

if not characters_list:
    st.write('Não há personagens cadastrados.')

else:
    character_selected = st.selectbox('Selecione um personagem',character_names,placeholder='Selecione um personagem',index=st.session_state['character_index'])

    if(not character_selected and not st.session_state['selected_character']):
        st.write('Nenhum personagem selecionado')

    elif(character_selected):
        st.session_state['selected_character'] = True
        st.session_state['selected_character_name'] = character_selected
        st.session_state['character_index'] = character_names.index(character_selected)
        character_index = st.session_state['character_index']

        st.title(characters_list[character_index][0])

        list_of_columns_job_species = st.columns(2)
        list_of_columns_job_species[0].subheader(f'{list_of_properties[1]}: {characters_list[character_index][1]}')
        list_of_columns_job_species[1].subheader(f'{list_of_properties[2]}: {characters_list[character_index][2]}')
#        with st.container(height=input_number_pixels, key='Teste', border=False):

        list_of_columns_properties = st.columns(4,gap='small',border=True)
        list_of_columns_properties[0].number_input(f'**HP (Max {characters_list[character_index][4]})**',0,value=int(characters_list[character_index][5]), key=f'hp_score_{characters_list[character_index][0]}')

#        list_of_columns_properties[1].write(f'**{list_of_properties[1]}**  \n{characters_list[character_index][1]}')
#        list_of_columns_properties[2].write(f'**{list_of_properties[2]}**  \n{characters_list[character_index][2]}')

        list_of_columns_properties[1].number_input(f'**XP**', 0, value=int(characters_list[character_index][3]), key=f'xp_score_{characters_list[character_index][0]}')
        list_of_columns_properties[2].number_input(f'**Movimento**',0,value=int(characters_list[character_index][10]), key=f'mov_score_{characters_list[character_index][0]}')
        list_of_columns_properties[3].number_input(f'**Defesa**',0,value=int(characters_list[character_index][11]), key=f'def_score_{characters_list[character_index][0]}')
        
        list_of_columns_atributes = st.columns(4,gap='small' ,border=True)
        list_of_columns_atributes[0].number_input(f'**{list_of_properties[6]}**',0,value=int(characters_list[character_index][6]),key=f'str_score_{characters_list[character_index][0]}')
        list_of_columns_atributes[1].number_input(f'**{list_of_properties[7]}**',0,value=int(characters_list[character_index][7]),key=f'agi_score_{characters_list[character_index][0]}')
        list_of_columns_atributes[2].number_input(f'**{list_of_properties[8]}**',0,value=int(characters_list[character_index][8]),key=f'lgc_score_{characters_list[character_index][0]}')
        list_of_columns_atributes[3].number_input(f'**{list_of_properties[9]}**',0,value=int(characters_list[character_index][9]),key=f'spr_score_{characters_list[character_index][0]}')

        if(int(characters_list[character_index][6]) > 1):
            list_of_columns_atributes[0].write(f'+**{floor(int(characters_list[character_index][6])/2)}** de defesa')
        else:
            list_of_columns_atributes[0].write(f'+**0** de defesa')
           
        if(int(characters_list[character_index][7]) > 1):
            list_of_columns_atributes[1].write(f'+**{floor(int(characters_list[character_index][7])/2)}** em rolagens de combate')
        else:
            list_of_columns_atributes[1].write(f'+**0** em rolagens de combate')
           
        if(int(characters_list[character_index][8]) > 1):
            list_of_columns_atributes[2].write(f'+**{floor(int(characters_list[character_index][8])/2)}** em rolagens fora de combate')
        else:
            list_of_columns_atributes[2].write(f'+**0** em rolagens fora de combate')
           
        if(int(characters_list[character_index][9]) > 1):
            list_of_columns_atributes[3].write(f'+**{floor(int(characters_list[character_index][9])/2)}** contrato com espírito')
        else:
            list_of_columns_atributes[3].write(f'+**0** contrato com espírito')
           

        if(int(st.session_state[f'xp_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][3]) or
           int(st.session_state[f'hp_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][5]) or
           int(st.session_state[f'str_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][6]) or
           int(st.session_state[f'agi_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][7]) or
           int(st.session_state[f'lgc_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][8]) or
           int(st.session_state[f'spr_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][9]) or
           int(st.session_state[f'mov_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][10]) or
           int(st.session_state[f'def_score_{characters_list[character_index][0]}']) != int(characters_list[character_index][11])):
            st.session_state['disabled_button'] = False
            print(f'hey got here {st.session_state['i']}')
            st.session_state['i'] += 1

        else:
            st.session_state['disabled_button'] = True

        apply_changes_button = st.button('Aplicar mudanças',disabled=st.session_state['disabled_button'],key='apply_changes')

        if(st.session_state['apply_changes']):
            try:
                db().update_character_atributes(characters_list[character_index][0],
                                                st.session_state[f'hp_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'str_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'agi_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'lgc_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'spr_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'mov_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'def_score_{characters_list[character_index][0]}'],
                                                st.session_state[f'xp_score_{characters_list[character_index][0]}'])
                st.warning('Atualizando ficha. Aguarde...')
                sleep(3)
            except:
                st.warning('Algo de errado aconteceu.')
                sleep(3)
            st.switch_page('interface/view_sheets.py')

#        for j in range(len(list_of_properties)):
#            if((j<6 or j>9) and j!=0 and j!=4 and j!=5):
#                st.write(f'{list_of_properties[j]}: {characters_list[character_index][j]}')
#        skill_categories = characters_list[character_index][-1].split(",")

        st.title('Equipamentos')

        items_by_character = db().list_items_by_character(characters_list[character_index][0])

        if items_by_character:
            st.session_state['items_by_character_flag'] = True
        else:
            st.session_state['items_by_character_flag'] = False

        items_buttons_columns = st.columns(2)
        items_buttons_columns[0].button('Cadastrar novo Equipamento',key='register_item_button')
        items_buttons_columns[1].button('Editar Equipamento',key='edit_item_button', disabled=(not st.session_state['items_by_character_flag']))

        if(st.session_state['register_item_button']):
            st.session_state['register_item'] = True
            st.session_state['edit_item'] = False
            st.switch_page('interface/register_item.py')

        if(st.session_state['edit_item_button']):
            st.session_state['register_item'] = False
            st.session_state['edit_item'] = True
            st.session_state['items_by_character'] = items_by_character
            st.switch_page('interface/register_item.py')

        list_of_items_tabs = st.session_state['items_categories']

        items_tabs = st.tabs(list_of_items_tabs)
        for i in range(len(items_tabs)):
            with items_tabs[i]:
                if not st.session_state['items_by_character_flag']:
                    st.write('Não há itens cadastrados para este personagem.')
                else:
                    for item in items_by_character:
                        if(list_of_items_tabs[i] == item['categoria']):
                            st.subheader(item['item']['nome'])
                            st.write(item['item']['desc'])
                            st.divider()

        st.title('Conhecimentos')

        abilities_by_character = db().list_abilities_by_character(characters_list[character_index][0])
        abilities_categories_by_character = db().list_abilities_categories_by_character(characters_list[character_index][0])
        abilities_categories_by_character_formated = []

        if(abilities_by_character):
            st.session_state['abilities_by_character_flag'] = True
        else:
            st.session_state['abilities_by_character_flag'] = False

        abilities_buttons_columns = st.columns(2)
        abilities_buttons_columns[0].button('Cadastrar novo Conhecimento',key='register_ability_button')
        abilities_buttons_columns[1].button('Editar Conhecimento',key='edit_ability_button',disabled=(not st.session_state['abilities_by_character_flag']))

        list_of_tabs = []
        for category in abilities_categories_by_character:
            list_of_tabs.append(category[0])
            abilities_categories_by_character_formated.append(category[0])

#        register_ability = st.button('Cadastrar novo Conhecimento')

        st.session_state['character_name'] = characters_list[character_index][0]
        st.session_state['abilities_categories_by_character'] = abilities_categories_by_character_formated

        if(st.session_state['register_ability_button']):
            st.session_state['register_ability'] = True
            st.session_state['edit_ability'] = False
            st.switch_page('interface/register_ability.py')

        if(st.session_state['edit_ability_button']):
            st.session_state['register_ability'] = False
            st.session_state['edit_ability'] = True
            st.session_state['abilities_by_character'] = abilities_by_character
            st.switch_page('interface/register_ability.py')

        tabs = st.tabs(list_of_tabs)
        for i in range(len(tabs)):
            with tabs[i]:
                if not abilities_by_character:
                    st.write('Não há conhecimentos cadastrados para este personagem.')
                else:
                    for ability in abilities_by_character:
                        if list_of_tabs[i] == ability['categoria']:
                            st.subheader(ability['habilidade']['nome'])
                            st.write(ability['habilidade']['desc'])
                            st.divider()
                        elif list_of_tabs[i] != ability['categoria'] and not ability['categoria']:
                            st.write('Não há Conhecimento cadastrado nesta categoria.')

    else:
        st.write('Ocorreu um problema, contate o administrador do sistema')
