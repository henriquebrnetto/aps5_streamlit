import streamlit as st
import requests

st.set_page_config(page_title="Login")
st.session_state['auth_status'] = False

pages = st.source_util.get_pages('app.py')
for k, val in pages.items():
    if val['page_name'] == 'app':
        val['page_name'] = '🔒_Login'

st.title("Login")

with st.form("login_form"):
    user = st.text_input("E-mail:")
    psswd = st.text_input("Senha:", type='password')
    sub = st.form_submit_button("Entrar")

if sub:
    infos = requests.get('---------------URL DO HEROKU---------------')
    try:
        infos = infos.json()
        emails = [dic['email'] for dic in infos]
        if not user:
            st.error('Preencha as informações necessárias.')
        elif user in emails:
            st.session_state['auth_status'] = True
            st.switch_page('pages/1_🏠_Página_Inicial.py')
        else:
            st.error('Sinto muito, você não está cadastrado.')

    except requests.exceptions.JSONDecodeError as e:
        st.error('Erro no servidor, tente novamente mais tarde.')

row = st.columns(4)
for col in row:
    c = col.container(border=True)
    c.page_link("pages/3_🧑_Criar_Usuário.py", label='Fazer Cadastro')
    break