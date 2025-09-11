import streamlit as st
from db_sqlite import buscar_cidades_e_estado
from db_mongo import inserir_local

def exibe_form_cadastra_local():
    cidades_e_estados = buscar_cidades_e_estado()
    mapa_cidades = {cidade: estado for cidade, estado in cidades_e_estados}
    nomes_cidades = list(mapa_cidades.keys())
    st.header("Cadastrar Novo Local de Interesse")

    cidade_selecionada = st.selectbox("Selecione a Cidade", nomes_cidades)
    estado_preenchido = mapa_cidades.get(cidade_selecionada, "")
    st.text_input("Estado", value=estado_preenchido, disabled=True)

    with st.form(key='form_local'):
        nome_local = st.text_input("Nome do Local")
        descricao = st.text_area("Descrição")
        latitude = st.number_input("Latitude", format="%.6f")
        longitude = st.number_input("Longitude", format="%.6f")
        
        submit_local_button = st.form_submit_button("Cadastrar Local")

        if submit_local_button:
            local_doc = {
                "nome local": nome_local,
                "cidade": cidade_selecionada, 
                "estado": estado_preenchido, 
                "coordenadas": {
                    "latitude": latitude,
                    "longitude": longitude
                },
                "descricao": descricao
            }
            inserir_local(local_doc)
            st.success(f"Local '{nome_local}' cadastrado com sucesso!")