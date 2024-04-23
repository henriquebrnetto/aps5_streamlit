import streamlit as st
from time import sleep
import requests

st.set_page_config(page_title="Buscar Usuário", layout="wide")

if 'search_button_user' not in st.session_state:
    st.session_state['search_button_user'] = False

st.page_link('./1_🏠_Página_Inicial.py')
st.title('Buscar Usuário')

with st.form("buscar_usuario_form"):
    id = st.text_input('Id do Usuário:')
    sub = st.form_submit_button('Buscar')

if sub:
    st.session_state['search_button_user'] = True

if st.session_state['search_button_user']:
    usuarios = requests.get('https://aps5-bucci-ikawa-4a310cd3a1d2.herokuapp.com/usuarios').json()


    infos = requests.get(f'https://aps5-bucci-ikawa-4a310cd3a1d2.herokuapp.com/usuarios/{id}')

    if infos.status_code == 200:
        infos = infos.json()
        with st.form("alterar_usuario_form"):

            nome = st.text_input("Nome:", infos['nome'])
            cpf = st.text_input("CPF:", infos['cpf'])
            data_nascimento = st.date_input("Data de Nascimento:", infos['data_nascimento'])

            update = st.form_submit_button("Atualizar Informações")
            delete = st.form_submit_button("Deletar Usuário")

            if update:
                info = {
                            'nome' : nome,
                            'cpf' : cpf,
                            'data_nascimento' : data_nascimento
                        }
                
                if cpf == infos['cpf']:
                    del info['Usuario']['cpf']

                infos = requests.put(f'https://aps5-bucci-ikawa-4a310cd3a1d2.herokuapp.com/usuarios/{id}', json=info)
                if infos.status_code == 200:
                    st.info(f"As informações do usuário com e-mail \"{id}\" foram atualizadas com sucesso.")
                
                elif infos.status_code == 400:
                    st.error(f"Verifique as informações inseridas.")
                
                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")
            
            if delete:
                infos = requests.delete(f'https://aps5-bucci-ikawa-4a310cd3a1d2.herokuapp.com/usuarios/{id}')

                if infos.status_code == 200:
                    st.info(f"O usuário com e-mail \"{id}\" foi deletado com sucesso.")

                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")

    elif infos.status_code == 404:
        st.error(f"Usuário com email \"{id}\" não encontrado.")

    elif infos.status_code == 500:
        st.error(f"Erro no servidor, tente novamente mais tarde.")