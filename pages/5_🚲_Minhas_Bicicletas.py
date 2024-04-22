import streamlit as st
from time import sleep
import requests
import pandas as pd

st.set_page_config(page_title="Minhas Bicicletas", layout="wide")

if 'auth_status' not in st.session_state or not st.session_state.auth_status:
    st.info('Por favor, faça o login ou faça o cadastro.')
    sleep(3)
    st.switch_page('./app.py')

st.title('Minhas Bicicletas')

infos = requests.get('https://asp3-gabarito-720a4403f44a.herokuapp.com/livros')
try:
    infos = pd.DataFrame(infos.json())
    infos.columns = ['ID', 'Título', 'Autor', 'Ano de Publicação', 'Gênero']
    infos.sort_values(by='ID', inplace=True, ignore_index=True)
    st.table(infos)
    
except requests.exceptions.JSONDecodeError as e:
    st.error('Erro no servidor, tente novamente mais tarde.')