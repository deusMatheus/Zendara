#####################################################################################################################
#                   Fichas de Zendara                   
# Versão 0.1.3
#
# Atualmente:
#
#   - Permite visualizar fichas. No momento há 2 personagens cadastrados para comparar com diferentes
#       habilidades e vocações.
# 
# Para modificar: 
#
#   - Não permite criar fichas, foi retirado para apresentar para o Lucas. Acrescentar novamente na próxima atualização.
#
#   - Verificar se será necessário mantes o ID das habilidades na tabela de character_sheets. 
#
#   - Tirar do preenchimento na criação da ficha XP, HP atual, Equipamentos, Armas e Armaduras
#
#   - Colocar Adicionar XP, Modificar HP atual, Adicionar Equipamentos, Adicionar Armas e
#       Adicionar Armaduras no Visualizador de Fichas.
#
#   - Os itens acima serão setados, inicialmente, com: 0XP, HP atual = função get_total_xp() no
#       set inicial durante a criação da ficha, Equipamentos = Armas = Armaduras = 'empty'.
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

if 'characters_list' not in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

if 'abilities_categories_list' not in st.session_state:
    st.session_state['abilities_categories_list'] = db().select_values("*",'abilities_categories')

if 'abilities_list' not in st.session_state:
    st.session_state['abilities_list'] = db().select_values("*",'abilities')


#print(st.session_state['characters_list'])
#print(st.session_state['abilities_categories_list'])
#print(st.session_state['abilities_list'])

pages = [
    st.Page('interface/public_page.py', title='Página inicial'),
#    st.Page('interface/create_sheets.py', title='Criador de Fichas'),
    st.Page('interface/view_sheets.py', title='Visualizador de Fichas'),
    ]
pg = st.navigation(pages)
pg.run()


