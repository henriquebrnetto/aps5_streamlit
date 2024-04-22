import streamlit as st
from time import sleep
import requests

st.set_page_config(page_title="Adicionar Bicicleta", layout="wide")

if 'auth_status' not in st.session_state or not st.session_state.auth_status:
    st.info('Por favor, faça o login ou faça o cadastro.')
    sleep(3)
    st.switch_page('./app.py')

st.title('Adicionar Bicicleta')

with st.form("criar_bike_form"):
    marca = st.text_input("Marca:")
    modelo = st.text_input("Modelo:")
    cidade = st.text_input("Cidade:")
    disponibilidade = st.radio(
    "Disponibilidade",
    ["Disponivel", "Indisponivel"]
)


    sub = st.form_submit_button("Cadastrar")

if sub:
    info = {
            'marca' : marca,
            'modelo' : modelo,
            'cidade' : cidade,
            'disponibilidade' : disponibilidade
            }
    
    if '' in info.values():
        st.error('Insira as informações necessárias.')

    else:
        infos = requests.post('https://asp3-gabarito-720a4403f44a.herokuapp.com/livros', json=info)
        if infos.status_code == 500:
            st.error('Erro no servidor. Tente novamente mais tarde.')
        elif infos.status_code == 201:
            st.info('Livro cadastrado com sucesso.')
        elif infos.status_code == 400:
            st.error('Verifique as informações inseridas.')
 