import streamlit as st
from time import sleep
import requests

st.set_page_config(page_title="Buscar Usuário", layout="wide")

if 'auth_status' not in st.session_state or not st.session_state.auth_status:
    st.info('Por favor, faça o login ou faça o cadastro.')
    sleep(3)
    st.switch_page('./app.py')

if 'search_button_user' not in st.session_state:
    st.session_state['search_button_user'] = False

st.title('Buscar Usuário')

with st.form("buscar_usuario_form"):
    email = st.text_input('E-mail:')
    sub = st.form_submit_button('Buscar')

if sub:
    st.session_state['search_button_user'] = True

if st.session_state['search_button_user']:
    usuarios = requests.get('https://asp3-gabarito-720a4403f44a.herokuapp.com/usuarios').json()

    id = None
    for dic in usuarios:
        if dic['email'] == email:
            id = dic['id']
    
    infos = requests.get(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/usuarios/{id}')

    if infos.status_code == 200:
        infos = infos.json()
        with st.form("alterar_usuario_form"):

            nome = st.text_input("Nome:", infos['nome'])
            user = st.text_input("E-mail:", infos['email'])
            cpf = st.text_input("CPF:", infos['cpf'])

            update = st.form_submit_button("Atualizar Informações")
            delete = st.form_submit_button("Deletar Usuário")

            if update:
                info = {
                        'Usuario' :
                            {
                            'nome' : nome,
                            'email' : user,
                            'cpf' : cpf
                            }
                        }
                
                if cpf == infos['cpf']:
                    del info['Usuario']['cpf']

                infos = requests.put(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/usuarios/{id}', json=info)
                if infos.status_code == 200:
                    st.info(f"As informações do usuário com e-mail \"{email}\" foram atualizadas com sucesso.")
                
                elif infos.status_code == 400:
                    st.error(f"Verifique as informações inseridas.")
                
                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")
            
            if delete:
                infos = requests.delete(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/usuarios/{id}')

                if infos.status_code == 200:
                    st.info(f"O usuário com e-mail \"{email}\" foi deletado com sucesso.")

                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")

    elif infos.status_code == 404:
        st.error(f"Usuário com email \"{email}\" não encontrado.")

    elif infos.status_code == 500:
        st.error(f"Erro no servidor, tente novamente mais tarde.")