import streamlit as st
from time import sleep
import requests

st.set_page_config(page_title="Criar emprestimo", layout="wide")

st.title('Criar Novo Empréstimo')
 

def add_loan(user_id, bike_id):
    try:
        response = requests.post(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/emprestimos/usuarios/{user_id}/bikes/{bike_id}')
        if response.status_code == 200:
            st.success('Empréstimo adicionado com sucesso!')
        else:
            st.error('Falha ao adicionar empréstimo.')
    except requests.exceptions.RequestException as e:
        st.error(f'Erro de rede: {e}')


st.header("Adicionar Empréstimo")
user_id = st.text_input("ID do Usuário para adicionar empréstimo", "")
bike_id = st.text_input("ID da Bicicleta para adicionar empréstimo", "")
if st.button("Adicionar Empréstimo"):
    add_loan(user_id, bike_id)