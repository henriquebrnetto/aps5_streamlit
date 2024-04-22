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
    titulo = st.text_input("Título:")
    autor = st.text_input("Autor:")
    ano_publicacao = st.text_input("Ano de Publicação:")
    
    opt = ('Comédia', 'Terror', 'Romance', 'Drama')
    genero = st.selectbox("Gênero do Livro:", opt)
    sub = st.form_submit_button("Cadastrar")

if sub:
    info = {
        'Livro' :
            {'titulo' : titulo,
            'autor' : autor,
            'anopublicacao' : ano_publicacao,
            'genero' : genero}
    }
    
    if '' in info['Livro'].values():
        st.error('Insira as informações necessárias.')

    else:
        infos = requests.post('https://asp3-gabarito-720a4403f44a.herokuapp.com/livros', json=info)
        if infos.status_code == 500:
            st.error('Erro no servidor. Tente novamente mais tarde.')
        elif infos.status_code == 201:
            st.info('Livro cadastrado com sucesso.')
        elif infos.status_code == 400:
            st.error('Verifique as informações inseridas.')
 