#####################################################################################################################
#                   Fichas de Zendara                   
# Versão 0.1.2
#
# Atualmente:
#
#   - Permite criar fichas simples e visualizá-las, mas alguns campos de texto da criação de ficha
#       devem ser movidos para a sessão de visualização, como descrito na sessão abaixo. 
# 
# Para modificar: 
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

list_of_properties = ["Nome", "Espécie","Vocação","Nível","HP máximo", "Hp atual","Força","Agilidade","Raciocínio","Espiritualidade","Movimento","Equipamentos","Armas","Armadura","Condição"]

# Com este CSS é possível estilizar a página pegando as classes dos componentes. 
#with open ('styles/styles.css') as file:
#    css = file.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

if 'characters_list' not in st.session_state:
    st.session_state['characters_list'] = db().select_values("*",'character_sheets')

pages = [
    st.Page('interface/public_page.py', title='Página inicial'),
    st.Page('interface/create_sheets.py', title='Criador de Fichas'),
    st.Page('interface/view_sheets.py', title='Visualizador de Fichas'),
    ]
pg = st.navigation(pages)
pg.run()


