import streamlit as st
from db_sqlite import criar_tabela_cidades, inserir_cidade

def exibe_form_cadastra_cidade():
    criar_tabela_cidades()


    if 'lat_origem' not in st.session_state:
        st.session_state.lat_origem = -7.11532

    if 'lon_origem' not in st.session_state:
        st.session_state.lon_origem = -34.861


    st.set_page_config(layout="wide")
    st.title("Projeto de Persistência Poliglota com Streamlit")


    st.header("Cadastrar Nova Cidade")
    with st.form(key='form_cidade'):
        cidade_input = st.text_input("Nome da Cidade")
        estado_input = st.text_input("Estado")
        submit_cidade_button = st.form_submit_button("Cadastrar Cidade")

        if submit_cidade_button:
            if cidade_input and estado_input:
                inserir_cidade(cidade_input, estado_input)
                st.success(f"Cidade '{cidade_input}' cadastrada com sucesso!")
            else:
                st.error("Por favor, preencha todos os campos.")