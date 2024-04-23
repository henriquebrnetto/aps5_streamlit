import streamlit as st
import requests

import streamlit as st
from time import sleep
import os

st.set_page_config(page_title="Página Inicial", layout="wide")

st.title('Bem-vindo')

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)

pages = os.listdir('pages/')
i = 0
for col in row1 + row2 + row3:
    try:
        tile = col.container(height=120)
        tile.page_link('pages/' + pages[i], icon=pages[i][2])
        i+=1
    except IndexError:
        pass