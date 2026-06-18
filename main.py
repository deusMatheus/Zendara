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