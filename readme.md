### Grupo:
Luiz Henrique da Silva Araujo, Kauã Douglas, Pedro Henrique

# Resumo da Arquitetura

- **app.py**: Este é o arquivo principal que inicia a aplicação. Ele importa e executa os componentes da interface do Streamlit.

- **componentes/**: Esta pasta agrupa os diferentes componentes da interface de usuário (Streamlit).

- **form_cadastra_cidade.py**: Define o formulário para adicionar novas cidades ao banco de dados SQLite.

- **form_cadastra_local.py**: Cria o formulário para cadastrar novos locais no banco de dados MongoDB.

- **proximidade_entre_locais.py**: Implementa a funcionalidade de busca de locais por proximidade, utilizando as coordenadas do MongoDB e a lógica de geoprocessamento.

- **visualiza_mapa.py**: Exibe os locais cadastrados no MongoDB em um mapa usando o Streamlit.

- **db_sqlite.py**: Gerencia a conexão e as operações (inserção e busca) no banco de dados SQLite.

- **db_mongo.py**: Gerencia a conexão e as operações no banco de dados MongoDB.

- **geoprocessamento.py**: Contém a função para calcular a distância geográfica entre dois pontos.

- **dados.db**: É o arquivo do banco de dados SQLite, onde as informações de cidades e estados são armazenadas.


```
├── componentes/
│   ├── form_cadastra_cidade.py
│   ├── form_cadastra_local.py
│   ├── proximidade_entre_locais.py
│   └── visualiza_mapa.py
├── .vscode/
│   └── settings.json
├── .gitignore
├── app.py
├── dados.db
├── db_mongo.py
├── db_sqlite.py
├── geoprocessamento.py
├── readme.md
└── requirements.txt
```


## Consultas ao SQLite
### O módulo db_sqlite.py contém as funções para interagir com o banco de dados SQLite.

1. Inserir uma nova cidade:
A função inserir_cidade é chamada para adicionar uma nova cidade e seu estado à tabela cidades.

```python
def inserir_cidade(cidade, estado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cidades (cidade, estado) VALUES (?, ?)", (cidade, estado))
    conn.commit()
    conn.close()
```
2. Buscar cidades e estados cadastrados:
A função buscar_cidades_e_estado consulta a tabela cidades para retornar todas as cidades e seus respectivos estados.

```python
def buscar_cidades_e_estado():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT cidade, estado FROM cidades")
    cidades_e_estados = cursor.fetchall()
    conn.close()
    return cidades_e_estados
```
## Consultas ao MongoDB
### O módulo db_mongo.py gerencia a interação com a coleção de locais no MongoDB.

1. Inserir um novo local:
A função inserir_local insere um novo documento na coleção de locais, incluindo o nome, cidade, estado, coordenadas e descrição.

```python
def inserir_local(local_doc):
    locais_collection = conectar_mongo()
    if locais_collection is not None:
        locais_collection.insert_one(local_doc)
```
2. Buscar todos os locais:
A função buscar_locais é utilizada para recuperar todos os documentos da coleção.

```python
def buscar_locais():
    locais_collection = conectar_mongo()
    if locais_collection is not None:
        return list(locais_collection.find())
    return []
```

3. Buscar locais próximos (geoprocessamento):
A funcionalidade de proximidade calcula a distância de cada local do MongoDB em relação a um ponto de origem, filtrando e exibindo aqueles que estão dentro de um raio especificado.

```python
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
```
## Prints de Funcionamento

### Cadastro de Cidades/Estados e Locais

<img width="1917" height="1046" alt="image" src="https://github.com/user-attachments/assets/eda37e4f-d45e-4d5a-905f-0be855b0c738" />

### visualização de locais no mapa e em listagem

<img width="1918" height="1043" alt="image" src="https://github.com/user-attachments/assets/826fc98e-7b8d-4000-b595-9c88792c9142" />

### visualização de proximidade entre locias 

<img width="1919" height="1044" alt="image" src="https://github.com/user-attachments/assets/40b4a5cb-9e18-4c20-9fb9-4256a6844280" />



