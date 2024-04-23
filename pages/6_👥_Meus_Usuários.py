import streamlit as st
from time import sleep
import requests
import pandas as pd

st.set_page_config(page_title="Meus Usuários", layout="wide")

st.page_link('./1_🏠_Página_Inicial.py')
st.title('Meus Usuários')

infos = requests.get('http://127.0.0.1:5000/usuarios')
try:
    print(infos.json())
    infos = pd.DataFrame(infos.json()['usuarios'], columns=['_id', 'nome', 'cpf', 'data_nascimento'])
    infos.sort_values(by='_id', inplace=True, ignore_index=True)
    st.table(infos)
    
except requests.exceptions.JSONDecodeError as e:
    st.error('Erro no servidor, tente novamente mais tarde.')