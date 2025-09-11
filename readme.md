
# Projeto de Persistência Poliglota

## Descrição do Projeto

Este projeto tem como objetivo desenvolver uma aplicação de **persistência poliglota** utilizando **SQLite** e **MongoDB** para armazenar e consultar dados em diferentes contextos. A aplicação também implementa recursos de **geoprocessamento** para manipular e visualizar dados espaciais, como latitude e longitude. A interface é construída com **Streamlit**, oferecendo uma experiência interativa e visual.

## Requisitos e Funcionalidades

### Banco de Dados

  * **SQLite**: Usado para armazenar dados tabulares estruturados, como informações de usuários, cidades, estados e países.
  * **MongoDB**: Usado para armazenar documentos no formato JSON, incluindo coordenadas geográficas (latitude e longitude) e metadados associados

### Geoprocessamento

  * Cálculo da distância entre dois pontos geográficos
  * Listagem de locais em um raio de distância a partir de uma coordenada fornecida
  * Consulta de dados do MongoDB e cruzamento de informações com dados do SQLite

### Interface (Streamlit)

A interface interativa permite:

  * Inserir novos dados no SQLite e no MongoDB
  * Selecionar uma cidade/estado do SQLite e visualizar os pontos de interesse correspondentes do MongoDB
  * Visualizar locais em um mapa (usando `st.map()`, Folium ou Pydeck)
  * Exibir resultados de consultas de geoprocessamento, como locais a até uma distância especificada a partir de uma coordenada.

## Tecnologias e Bibliotecas

  * Python 3.10+ 
  * Streamlit (interface) 
  * SQLite3 (banco relacional) 
  * PyMongo (integração com MongoDB) 
  * Geopy (cálculo de distâncias) 
  * Folium ou Pydeck (visualização de mapas) 
  * Pandas (manipulação de dados) 


## Como Executar

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Crie o arquivo `.env`** com a sua string de conexão do MongoDB:
    ```
    MONGO_URI="mongodb://<seu_usuario>:<sua_senha>@<seu_host>:<sua_porta>/?authSource=admin"
    ```
3.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Prints de Funcionamento

### Cadastro de Cidades/Estados e Locais

<img width="1917" height="1046" alt="image" src="https://github.com/user-attachments/assets/eda37e4f-d45e-4d5a-905f-0be855b0c738" />

### visualização de locais no mapa e em listagem

<img width="1918" height="1043" alt="image" src="https://github.com/user-attachments/assets/826fc98e-7b8d-4000-b595-9c88792c9142" />

### visualização de proximidade entre locias 

<img width="1919" height="1044" alt="image" src="https://github.com/user-attachments/assets/40b4a5cb-9e18-4c20-9fb9-4256a6844280" />



