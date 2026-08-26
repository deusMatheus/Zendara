import streamlit as st
from time import sleep
from classes.db_manager import db_manager as db

st.session_state['register_ability'] = False
st.session_state['edit_ability'] = False

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

def editItems(oldItemName, newItemName, newItemDesc, newItemCateg, characterName):
    if(oldItemName != '' and newItemName != '' and newItemDesc != '' and newItemCateg != '' and characterName != ''):
        try:
            db().update_item(oldItemName, newItemName, newItemDesc, newItemCateg, characterName)
            st.write('Edição de item concluída!')
            st.toast('Edição de item concluída!')
            st.toast('Edição de item concluída!')
        except:
            st.toast('Algo de errado aconteceu.')
    sleep(1)
    st.session_state['edit_item'] = False
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

if(st.session_state['edit_item']):
    character_name = st.session_state['character_name']
    edit_item_category = ''
    edit_item_name = ''
    edit_item_desc = ''
    st.title(f'Selecione um item de {character_name} para editar')
    items_list_names = []
    for item in st.session_state['items_by_character']:
        items_list_names.append(item['item']['nome'])
    selected_item = st.selectbox('Selecione um item',items_list_names,placeholder='Selecione um item',index=None)

    if(not selected_item):
        st.write('Nenhum item selecionado')
    elif(selected_item):
        for item in st.session_state['items_by_character']:
            if(selected_item in item['item']['nome']):
#                st.write(item)
                edit_item_category = item['categoria']
                edit_item_name = item['item']['nome']
                edit_item_desc = item['item']['desc']
        with st.form('edit_item_form'):
            new_item_name = st.text_input('Nome do item',value=edit_item_name,placeholder='Nome do item')
            new_item_desc = st.text_area('Descrição do item',value=edit_item_desc,placeholder='Descrição do item')
            new_item_categ = st.selectbox('Categoria do item',st.session_state['items_categories'],index=st.session_state['items_categories'].index(edit_item_category))
            if st.form_submit_button(label='Editar item'):
                st.session_state['edit_item'] = True
                editItems(edit_item_name, new_item_name, new_item_desc, new_item_categ, character_name)
    else:
        st.write('Ocorreu um erro. Contate o administrador do sistema.')

else:
    st.title("Ops!")
    st.write('Para registrar um item, primeiro selecione um personagem no **Visualizador de fichas** e clique no botão **Cadastrar novo item**.')

