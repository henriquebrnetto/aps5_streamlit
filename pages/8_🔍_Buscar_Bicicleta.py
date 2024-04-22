import streamlit as st
from time import sleep
import requests

st.set_page_config(page_title="Buscar Bicicleta", layout="wide")

if 'auth_status' not in st.session_state or not st.session_state.auth_status:
    st.info('Por favor, faça o login ou faça o cadastro.')
    sleep(3)
    st.switch_page('./app.py')

if 'search_button' not in st.session_state:
    st.session_state['search_button'] = False

st.title('Buscar Bicicleta')

with st.form("buscar_bicicleta_form"):
    id = st.text_input('ID da Bicicleta:')
    sub = st.form_submit_button('Buscar')

if sub:
    st.session_state['search_button'] = True

if st.session_state['search_button']:
    infos = requests.get(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/livros/{id}')

    if infos.status_code == 200:
        infos = infos.json()
        with st.form("alterar_bicicleta_form"):
            titulo = st.text_input("Título:", infos['titulo'])
            autor = st.text_input("Autor:", infos['autor'])
            ano_publicacao = st.text_input("Ano de Publicação:", infos['anopublicacao'])

            opt = ('Comédia', 'Terror', 'Romance', 'Drama')

            try:
                genero = st.selectbox("Gênero do Livro:", opt, opt.index(infos['genero']))
            except ValueError:
                opt += (infos['genero'],)
                genero = st.selectbox("Gênero do Livro:", opt, opt.index(infos['genero']))

            update = st.form_submit_button("Atualizar Informações")
            delete = st.form_submit_button("Deletar Livro")

            if len(opt) != 4:
                st.info("Favor alterar o gênero do livro para uma opção válida.")

            if update:
                info = {
                    'Livro' : {'titulo' : titulo,
                    'autor' : autor,
                    'anopublicacao' : ano_publicacao,
                    'genero' : genero
                    }
                }
                infos = requests.put(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/livros/{id}', json=info)
                if infos.status_code == 200:
                    st.info(f"As informações do Livro com ID={id} foram atualizadas com sucesso.")
                elif infos.status_code == 400:
                    st.error(f"Verifique as informações inseridas.")
                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")
            
            elif delete:
                infos = requests.delete(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/livros/{id}')
                if infos.status_code == 200:
                    st.info(f"O Livro com ID={id} foi deletado com sucesso.")
                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")

    elif infos.status_code == 404:
        st.error(f"Livro com ID={id} não encontrado.")
    elif infos.status_code == 500:
        st.error(f"Erro no servidor, tente novamente mais tarde.")