import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Define configurações de conexão ao banco
DB_SETTINGS = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")) if os.getenv("DB_PORT") else 5432,
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
}

# Define a URL base da API CoinCap
API_BASE_URL = os.getenv("API_BASE_URL")

# Exibe as variáveis carregadas (debug)
print("DB SETTINGS LIDOS DO .env:", DB_SETTINGS)
