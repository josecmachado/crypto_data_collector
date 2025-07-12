from db.models import create_tables
from api.coincap_client import CoinCapClient
from db.repository import insert_or_update_crypto

def main():
    create_tables()
    client = CoinCapClient()
    cryptos = client.get_assets(limit=10)

    if cryptos:
        insert_or_update_crypto(cryptos)
        print("Dados inseridos com sucesso!")
    else:
        print("Nenhum dado coletado.")

if __name__ == "__main__":
    main()
