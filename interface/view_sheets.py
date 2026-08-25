from time import sleep
import streamlit as st
#import tailwind as tw
from classes.db_manager import db_manager as db

if 'characters_list' in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

if 'register_form' not in st.session_state:
    st.session_state['register_form'] = False

st.session_state['register_ability'] = False
st.session_state['register_item'] = False

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
list_of_properties = ["Nome", "Espécie","Vocação","Pontos de Experiência","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento"]

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
        st.subheader(characters_list[character_index][0])
#        with st.container(height=135, key='Teste', border=False):
        st.number_input(f'HP (Max {characters_list[character_index][4]})',0,value=int(characters_list[character_index][5]),width=int(135))
        list_of_columns = st.columns(4, border=True)
        list_of_columns[0].number_input(f'{list_of_properties[6]}',0,value=int(characters_list[character_index][6]),width=int(135))
        list_of_columns[1].number_input(f'{list_of_properties[7]}',0,value=int(characters_list[character_index][7]),width=int(135))
        list_of_columns[2].number_input(f'{list_of_properties[8]}',0,value=int(characters_list[character_index][8]),width=int(135))
        list_of_columns[3].number_input(f'{list_of_properties[9]}',0,value=int(characters_list[character_index][9]),width=int(135))
        for j in range(len(list_of_properties)):
            if((j<6 or j>9) and j!=0 and j!=4 and j!=5):
                st.write(f'{list_of_properties[j]}: {characters_list[character_index][j]}')
#        skill_categories = characters_list[character_index][-1].split(",")

        st.title('Equipamentos')

        register_item = st.button('Cadastrar novo Equipamento')

        if(register_item):
            st.session_state['register_item'] = True
            st.switch_page('interface/register_item.py')

        items_by_character = db().list_items_by_character(characters_list[character_index][0])

        list_of_items_tabs = ['Arma', 'Armadura', 'Mundano', 'Mágico']

        items_tabs = st.tabs(list_of_items_tabs)
        for i in range(len(items_tabs)):
            with items_tabs[i]:
                if not items_by_character:
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

        list_of_tabs = []
        for category in abilities_categories_by_character:
            list_of_tabs.append(category[0])
            abilities_categories_by_character_formated.append(category[0])

        register_ability = st.button('Cadastrar novo Conhecimento')

        st.session_state['character_name'] = characters_list[character_index][0]
        st.session_state['abilities_categories_by_character'] = abilities_categories_by_character_formated
        if(register_ability):
            st.session_state['register_ability'] = True
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
                            st.write(f'_{ability['habilidade']['tipo']}_')
                            st.write(ability['habilidade']['desc'])
                            st.divider()
                        elif list_of_tabs[i] != ability['categoria'] and not ability['categoria']:
                            st.write('Não há Conhecimento cadastrado nesta categoria.')

    else:
        st.write('Ocorreu um problema, contate o administrador do sistema')
