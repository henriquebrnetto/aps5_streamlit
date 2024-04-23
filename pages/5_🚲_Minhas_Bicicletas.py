import streamlit as st
from time import sleep
import requests
import pandas as pd

def disponivel(val):
    return 'Disponível' if val == True else 'Em Uso'

st.set_page_config(page_title="Minhas Bicicletas", layout="wide")

st.page_link('./1_🏠_Página_Inicial.py')
st.title('Minhas Bicicletas')

infos = requests.get('https://aps5-bucci-ikawa-4a310cd3a1d2.herokuapp.com/bikes')
try:
    infos = pd.DataFrame(infos.json()['bicicletas'], columns=['_id', 'marca', 'modelo', 'cidade', 'disponibilidade'])
    infos['disponibilidade'] = infos['disponibilidade'].apply(disponivel)
    infos.sort_values(by='_id', inplace=True, ignore_index=True)
    st.table(infos)
    
except requests.exceptions.JSONDecodeError as e:
    st.error('Erro no servidor, tente novamente mais tarde.')