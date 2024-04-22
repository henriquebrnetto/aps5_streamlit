import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Meus Empréstimos", layout="wide")
st.title('Meus Empréstimos')

def display_loans():
    try:
        loans = requests.get('https://asp3-gabarito-720a4403f44a.herokuapp.com/emprestimos')
        loans = pd.DataFrame(loans.json())
        loans = loans[['id_usuario', 'id_bicicleta']]  # Ajuste para mostrar apenas IDs dos usuários e das bicicletas
        st.table(loans)
    except requests.exceptions.JSONDecodeError:
        st.error('Erro no servidor, tente novamente mais tarde.')


def delete_loan(user_id, bike_id):
    try:
        response = requests.delete(f'https://asp3-gabarito-720a4403f44a.herokuapp.com/emprestimos/usuarios/{user_id}/bikes/{bike_id}')
        if response.status_code == 200:
            st.success('Empréstimo deletado com sucesso!')
        else:
            st.error('Falha ao deletar empréstimo.')
    except requests.exceptions.RequestException as e:
        st.error(f'Erro de rede: {e}')



# User interface to delete loans
st.header("Deletar Empréstimo")
del_user_id = st.text_input("ID do Usuário do empréstimo para deletar", "")
del_bike_id = st.text_input("ID da Bicicleta do empréstimo para deletar", "")
if st.button("Deletar Empréstimo"):
    delete_loan(del_user_id, del_bike_id)

# Displaying all loans
st.header("Todos os Empréstimos")
display_loans()
