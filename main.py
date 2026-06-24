#####################################################################################################################
#                   Fichas de Zendara                   
# Versão 0.1.1
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
#   - Não há bugs conhecidos até o momento.
#
# Bugs resolvidos: 
#
#   - Não há bugs resolvidos até o momento.
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

pages = [
    st.Page('interface/public_page.py', title='Página inicial'),
    st.Page('interface/create_sheets.py', title='Criador de Fichas'),
    st.Page('interface/view_sheets.py', title='Visualizador de Fichas'),
    ]
pg = st.navigation(pages)
pg.run()

#table_name = st.text_input('Table Name')
#table_value = st.text_input('Table Value')
#
#button = st.button('Press me!')
#
#if(button):
#    db().create_table(f"{table_name}",(f"{table_value}",""))

#characters_list = db().select_values("*",'character_sheets')
##print(teste[1])
##st.write(teste[0])
#
##for i in range(len(list_of_properties)):
##    st.write(f'{list_of_properties[i]}: {teste[0][i]}')
#if not characters_list:
#    st.write('Não há fichas cadastradas.')
#
#else:
#    for character in characters_list:
#        st.divider()
#        for i in range(len(list_of_properties)):
#            st.write(f'{list_of_properties[i]}: {character[i]}')