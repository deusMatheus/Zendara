#####################################################################################################################
#                   Fichas de Zendara                   
# Versão 0.4.1
#
# Atualmente:
#
#   - Permite cadastrar e visualizar fichas. 
#
#   - Permite cadastrar e visualizar itens e habilidades para cada personagem.  
#
#   - Layout modificado, com atributos destacados na ficha.  
#
#   - Retiradas as colunas de equipamentos da tabela de personagenns.
#
#   - Permite editar atributos e HP dos personagens
#
#   - Permite editar itens dos personagens
#
#
#   - Permite editar habilidades dos personagens (necessita de mais testes)
#
# Para modificar: 
#
#   - Ajustar o layout da ficha
#
#   - Permitir criação de novas categorias de habilidades 
#
#   - Permitir alteração de XP e Movimento no Visualizador de Fichas.
#
#   - Colocar novas classes na pasta de Classes e realizar a comunicação com o DB por lá ao invés da pasta Interface.
#
#   - Permitir inserir imagens dos personagens
#
#   - Permitir backup por e-mail
#
#   - Permitir full reset
#
#   - Criar um log e armazenar no DB
#
#   - Limpar código comentado
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

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

#list_of_properties = ["Nome", "Espécie","Vocação","Nível","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura","Condição"]

# Com este CSS é possível estilizar a página pegando as classes dos componentes. 
#with open ('styles/styles.css') as file:
#    css = file.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.session_state['version'] = 'V 0.4.0'

if 'characters_list' not in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

if 'abilities_categories_list' not in st.session_state:
    st.session_state['abilities_categories_list'] = db().select_values("*",'abilities_categories')

if 'abilities_list' not in st.session_state:
    st.session_state['abilities_list'] = db().select_values("*",'abilities')

if 'register_ability' not in st.session_state:
    st.session_state['register_ability'] = False

if 'edit_ability' not in st.session_state:
    st.session_state['edit_ability'] = False

if 'register_item' not in st.session_state:
    st.session_state['register_item'] = False

if 'edit_item' not in st.session_state:
    st.session_state['edit_item'] = False

if 'disabled_button' not in st.session_state:
    st.session_state['disabled_button'] = True

if 'apply_changes' not in st.session_state:
    st.session_state['apply_changes'] = False

if 'items_by_character' not in st.session_state:
    st.session_state['items_by_character'] = False

if 'abilities_by_character' not in st.session_state:
    st.session_state['abilities_by_character'] = False

if 'items_by_character_flag' not in st.session_state:
    st.session_state['items_by_character_flag'] = False

if 'abilities_by_character_flag' not in st.session_state:
    st.session_state['abilities_by_character_flag'] = False

if 'items_by_character' not in st.session_state:
    st.session_state['items_by_character'] = []

if 'items_categories' not in st.session_state:
    st.session_state['items_categories'] = ['Arma', 'Armadura', 'Mundano', 'Mágico']

#print(st.session_state['characters_list'])
#print(st.session_state['abilities_categories_list'])
#print(st.session_state['abilities_list'])

pages = [
    st.Page('interface/public_page.py', title='Página inicial'),
    st.Page('interface/create_sheets.py', title='Criador de Fichas'),
    st.Page('interface/view_sheets.py', title='Visualizador de Fichas'),
    st.Page('interface/register_ability.py', title='Registrar Habilidade'),
    st.Page('interface/register_item.py', title='Registrar Item')
    ]

pg = st.navigation(pages)
pg.run()


