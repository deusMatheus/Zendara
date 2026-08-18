#####################################################################################################################
#                   Fichas de Zendara                   
# Versão 0.1.4
#
# Atualmente:
#
#   - Permite cadastrar e visualizar fichas. 
#
#   - Permite cadastrar e visualizar habilidades para cada personagem.  
#
# Para modificar: 
#
#   - Ajustar o layout da ficha
#
#   - Permitir criação de novas categorias de habilidades 
#
#   - Colocar Adicionar XP, Modificar HP atual, Adicionar Equipamentos (armas e armaduras serão subitems)
#       no Visualizador de Fichas.
#   
#   - Fazer com itens igual as habilidades, onde existe uma tabela com o ID do personagem à quem o item
#       pertence. Separar em categorias como armas, armaduras, itens mundanos e mágicos.
#   
# Bugs conhecidos: 
#
#   - Não há bugs conhecidos no momento.
#
# Bugs resolvidos: 
#
#   - Ao selecionar visualizador de fichas (view_sheets.py), estava dobrando a quantidade de fichas na variavel
#       characters_list sempre que a página era acessada. Pegar esses dados do db foi colocado em main.py,
#       o que chama apenas uma única vez e é armazenado em st.session.
#
#####################################################################################################################

import streamlit as st
#import tailwind as tw
from classes.db_manager import db_manager as db

#st.set_page_config(layout="wide")

#list_of_properties = ["Nome", "Espécie","Vocação","Nível","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura","Condição"]

# Com este CSS é possível estilizar a página pegando as classes dos componentes. 
#with open ('styles/styles.css') as file:
#    css = file.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.session_state['version'] = 'V 0.1.4'

if 'characters_list' not in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

if 'abilities_categories_list' not in st.session_state:
    st.session_state['abilities_categories_list'] = db().select_values("*",'abilities_categories')

if 'abilities_list' not in st.session_state:
    st.session_state['abilities_list'] = db().select_values("*",'abilities')

if 'register_ability' not in st.session_state:
    st.session_state['register_ability'] = False

#print(st.session_state['characters_list'])
#print(st.session_state['abilities_categories_list'])
#print(st.session_state['abilities_list'])

pages = [
    st.Page('interface/public_page.py', title='Página inicial'),
    st.Page('interface/create_sheets.py', title='Criador de Fichas'),
    st.Page('interface/view_sheets.py', title='Visualizador de Fichas'),
    st.Page('interface/register_ability.py', title='Registrar Habilidade')
    ]

pg = st.navigation(pages)
pg.run()


