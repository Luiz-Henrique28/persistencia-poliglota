import sqlite3

# Conectar ao banco de dados SQLite
# O arquivo 'dados.db' será criado se não existir
def conectar():
    conn = sqlite3.connect('dados.db')
    return conn

# Criar a tabela de cidades e estados
def criar_tabela_cidades():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

# Inserir uma nova cidade
def inserir_cidade(cidade, estado):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cidades (cidade, estado) VALUES (?, ?)", (cidade, estado))
    conn.commit()
    conn.close()

# Consultar todas as cidades
def buscar_cidades_e_estado():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT cidade, estado FROM cidades")
    cidades_e_estados = cursor.fetchall()
    
    conn.close()
    #return [c[0] for c in cidades]
    return cidades_e_estados