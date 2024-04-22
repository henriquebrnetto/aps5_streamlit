import streamlit as st
from time import sleep
import os

st.set_page_config(page_title="Página Inicial", layout="wide")

if 'auth_status' not in st.session_state or not st.session_state.auth_status:
    st.info('Por favor, faça o login ou faça o cadastro.')
    sleep(3)
    st.switch_page('./app.py')

st.title('Bem-vindo')

row1 = st.columns(3)
row2 = st.columns(3)

pages = os.listdir('pages/')
i = 1
for col in row1 + row2:
    tile = col.container(height=120)
    tile.page_link('pages/' + pages[i], icon=pages[i][2])
    i+=1