from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Função para conectar ao MongoDB
def conectar_mongo():
    try:
        client = MongoClient(URI)
        client.admin.command('ping')
        db = client.locais_db
        return db.locais  # Retorna a coleção
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None

# Inserir um novo documento (local) na coleção
def inserir_local(local_doc):
    locais_collection = conectar_mongo()
    if locais_collection is not None:
        locais_collection.insert_one(local_doc)
        print("Documento inserido com sucesso!")
    else:
        print("Não foi possível inserir o documento. Conexão falhou.")

# Buscar todos os locais da coleção
def buscar_locais():
    locais_collection = conectar_mongo()
    if locais_collection is not None:
        return list(locais_collection.find())
    return []
