import streamlit as st
import pandas as pd

from db_mongo import buscar_locais

def visualiza_mapa():
    st.header("Visualizar Locais no Mapa")

    locais_mongo = buscar_locais()

    if locais_mongo:
        
        dados_mapa = []
        for local in locais_mongo:
            
            if 'coordenadas' in local:
                dados_mapa.append({
                    'latitude': local['coordenadas']['latitude'],
                    'longitude': local['coordenadas']['longitude'],
                    'nome': local.get('nome local', 'Não informado'),
                    'cidade': local.get('cidade', 'Não informado'),
                    'estado': local.get('estado', 'Não informado'),
                })
                print(local['coordenadas']['latitude'], local['coordenadas']['longitude'])

        
        df_locais = pd.DataFrame(dados_mapa)

        if not df_locais.empty:
            
            st.map(df_locais)

            
            st.subheader("Tabela de Locais Cadastrados")
            st.dataframe(df_locais)
        else:
            st.info("Nenhum local com coordenadas válidas encontrado para exibir no mapa.")
    else:
        st.info("Nenhum local cadastrado no MongoDB ainda.")