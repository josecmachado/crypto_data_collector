from db.models import create_tables
from db.repository import insert_or_update_cryptos
from api.coincap_client import CoinCapClient

def main():
    # Cria as tabelas se não existirem
    create_tables()

    # Instancia o client da API
    client = CoinCapClient()

    # Coleta dados da CoinCap
    assets = client.get_assets(limit=10)

    if assets:
        # Prepara os dados para salvar no banco
        prepared_data = client.prepare_crypto_data(assets)

        # Insere ou atualiza dados no banco
        insert_or_update_cryptos(prepared_data)
        print("Dados inseridos com sucesso!")
    else:
        print("Nenhum dado coletado.")

if __name__ == "__main__":
    main()
