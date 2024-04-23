import streamlit as st
import requests

st.set_page_config(page_title="Criar Usuário", layout="wide")

st.page_link('./1_🏠_Página_Inicial.py')
st.title('Criar Usuário')

with st.form("criar_usuario_form"):
    nome = st.text_input("Nome:")
    cpf = st.text_input("CPF:")
    data_nascimento = st.date_input("Data de Nascimento:")

    sub = st.form_submit_button("Cadastrar")

if sub:
    info = {
            'nome' : nome,
            'cpf' : cpf,
            'data_nascimento' : data_nascimento
        }

    if '' in info.values():
        st.error('Insira as informações necessárias.')

    else:
        infos = requests.post('https://aps5-bucci-ikawa-4a310cd3a1d2.herokuapp.com/usuarios', json=info)
        if infos.status_code == 500:
            st.error('Erro no servidor. Tente novamente mais tarde.')
        elif infos.status_code == 201:
            st.info('Usuário cadastrado com sucesso.')
        elif infos.status_code == 400:
            st.error('Verifique as informações inseridas.')
