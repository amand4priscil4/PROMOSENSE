import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()
uri = os.getenv("MONGO_URI")

# Conexão com o MongoDB Atlas
client = MongoClient(uri)

db = client["promosense"]
collection = db["avaliacoes"]

# Carregar o arquivo processado
df = pd.read_csv("data/processed/olist_processado.csv")

# Converter para dicionário e inserir no MongoDB
dados = df.to_dict(orient="records")
collection.insert_many(dados)

print(f"✅ {len(dados)} documentos inseridos no MongoDB!")