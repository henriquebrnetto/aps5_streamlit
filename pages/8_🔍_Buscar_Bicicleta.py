import streamlit as st
from time import sleep
import requests

st.set_page_config(page_title="Buscar Bicicleta", layout="wide")

if 'search_button' not in st.session_state:
    st.session_state['search_button'] = False

st.title('Buscar Bicicleta')

with st.form("buscar_bicicleta_form"):
    id = st.text_input('ID da Bicicleta:')
    sub = st.form_submit_button('Buscar')

if sub:
    st.session_state['search_button'] = True

if st.session_state['search_button']:
    infos = requests.get(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/bikes/{id}')

    if infos.status_code == 200:
        infos = infos.json()
        with st.form("alterar_bicicleta_form"):
            marca = st.text_input("Marca:", infos['marca'])
            modelo = st.text_input("Modelo:", infos['modelo'])
            cidade = st.text_input("Cidade:", infos['cidade'])
            disponibilidade = st.radio(
                "Disponibilidade",
                ["Disponivel", "Indisponivel"],
                index=int(infos['disponibilidade'])
            )


            update = st.form_submit_button("Atualizar Informações")
            delete = st.form_submit_button("Deletar Bike")


            if update:
                info = {
                    'marca' : marca,
                    'autor' : modelo,
                    'cidade' : cidade,
                    'disponibilidade' : disponibilidade
                    }
                

                infos = requests.put(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/bikes/{id}', json=info)
                if infos.status_code == 200:
                    st.info(f"As informações da Bike com ID={id} foram atualizadas com sucesso.")
                elif infos.status_code == 400:
                    st.error(f"Verifique as informações inseridas.")
                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")
            
            elif delete:
                infos = requests.delete(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/bikes/{id}')
                if infos.status_code == 200:
                    st.info(f"A bike com ID={id} foi deletado com sucesso.")
                elif infos.status_code == 500:
                    st.error(f"Erro no servidor, tente novamente mais tarde.")

    elif infos.status_code == 404:
        st.error(f"Bike com ID={id} não encontrado.")
    elif infos.status_code == 500:
        st.error(f"Erro no servidor, tente novamente mais tarde.")