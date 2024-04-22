import streamlit as st
from time import sleep
import requests
import pandas as pd

st.set_page_config(page_title="Minhas Bicicletas", layout="wide")

st.title('Minhas Bicicletas')

infos = requests.get('https://asp3-gabarito-720a4403f44a.herokuapp.com/livros')
try:
    infos = pd.DataFrame(infos.json())
    infos.columns = ['_id', 'marca', 'modelo', 'cidade', 'disponibilidade']
    infos.sort_values(by='_id', inplace=True, ignore_index=True)
    st.table(infos)
    
except requests.exceptions.JSONDecodeError as e:
    st.error('Erro no servidor, tente novamente mais tarde.')