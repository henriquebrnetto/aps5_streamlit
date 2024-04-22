import streamlit as st
import requests

st.set_page_config(page_title="Criar Usuário", layout="wide")

st.title('Criar Usuário')

with st.form("criar_usuario_form"):
    nome = st.text_input("Nome:")
    user = st.text_input("E-mail:")
    cpf = st.text_input("CPF:")
    sub = st.form_submit_button("Cadastrar")

if sub:
    info = {
        'Usuario' :
            {
            'nome' : nome,
            'email' : user,
            'cpf' : cpf
            }
    }

    if '' in info['Usuario'].values():
        st.error('Insira as informações necessárias.')

    else:
        infos = requests.post('https://asp3-gabarito-720a4403f44a.herokuapp.com/usuarios', json=info)
        if infos.status_code == 500:
            st.error('Erro no servidor. Tente novamente mais tarde.')
        elif infos.status_code == 201:
            st.info('Usuário cadastrado com sucesso.')
        elif infos.status_code == 400:
            st.error('Verifique as informações inseridas.')
