import streamlit as st
from time import sleep
from classes.db_manager import db_manager as db

items_categories = ['Arma', 'Armadura', 'Mundano', 'Mágico']

def registerItems(itemName, itemDesc, itemCateg, characterName):
    st.session_state['register_form_item'] = True
    if (itemName != '' and itemDesc != '' and itemCateg != '' and st.session_state['register_form_item']):
        try:
            db().create_item(itemName, itemDesc, itemCateg, characterName)
            st.write('Cadastro de item concluído!')
            st.toast('Cadastro de item concluído!')
            st.toast('Cadastro de item concluído!')
        except:
            st.toast('Algo de errado aconteceu.')
    sleep(1)
    st.session_state['register_item'] = False
    st.switch_page('interface/public_page.py')

if(st.session_state['register_item']):
    st.title(f'Registrar Item para {st.session_state['character_name']}')
    with st.form('register_item_form'):
        character_name = st.session_state['character_name'] 
        item_name = st.text_input('Nome do Item', placeholder='Nome do Conhecimento', key='items_name')
        item_desc = st.text_area('Descrição do Item', placeholder='Descrição do Conhecimento', key='items_desc')
        item_categ = st.selectbox('Selecione uma categoria', items_categories, placeholder='Selecione uma categoria', index=None, key='items_categ')
        st.session_state['register_item'] = True 
        if st.form_submit_button(label='Registrar'):
            registerItems(item_name, item_desc, item_categ, character_name)

else:
    st.title("Ops!")
    st.write('Para registrar um item, primeiro selecione um personagem no **Visualizador de fichas** e clique no botão **Cadastrar novo item**.')

