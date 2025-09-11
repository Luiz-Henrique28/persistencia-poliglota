import streamlit as st
import pandas as pd
from geoprocessamento import calcular_distancia_km
from db_mongo import buscar_locais

def proximidade_entre_locais():
    st.header("Função de Proximidade Geográfica")
    st.markdown("Busque locais próximos a um ponto de referência.")

    with st.form(key='form_proximidade'):
        lat_origem = st.number_input("Latitude de Referência", key='lat_origem', format="%.6f", )
        lon_origem = st.number_input("Longitude de Referência", key='lon_origem', format="%.6f", )

        raio_km = st.number_input("Raio de Distância (km)", min_value=1.0, value=10.0, step=1.0)
        
        submit_proximidade_button = st.form_submit_button("Buscar Locais Próximos")

        if submit_proximidade_button:
            lat_origem = st.session_state.lat_origem
            lon_origem = st.session_state.lon_origem

            print(f"Valor da Latitude: {lat_origem} | Tipo: {type(lat_origem)}")
            print(f"Valor da Longitude: {lon_origem} | Tipo: {type(lon_origem)}")

            locais_proximos = []
            
            locais_todos = buscar_locais() 
            
            coord_origem = {'latitude': lat_origem, 'longitude': lon_origem}

            for local in locais_todos:
                if 'coordenadas' in local:
                    coord_local = local['coordenadas']
                    
                    
                    if all(isinstance(coord_local.get(k), (int, float)) for k in ['latitude', 'longitude']):
                        distancia = calcular_distancia_km(coord_origem, coord_local)

                        if distancia <= raio_km:
                            
                            local['distancia_km'] = round(distancia, 2)
                            locais_proximos.append(local)
            
            if locais_proximos:
                st.success(f"Encontrados {len(locais_proximos)} locais em um raio de {raio_km} km.")
                
                
                df_proximos = pd.DataFrame(locais_proximos)
                df_proximos['latitude'] = df_proximos['coordenadas'].apply(lambda x: x['latitude'])
                df_proximos['longitude'] = df_proximos['coordenadas'].apply(lambda x: x['longitude'])
                
                
                st.map(df_proximos[['latitude', 'longitude']])
                st.dataframe(df_proximos[['nome local', 'cidade', 'distancia_km', 'descricao']])
            else:
                st.info("Nenhum local encontrado dentro do raio especificado.")