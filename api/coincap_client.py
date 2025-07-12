import requests
from config.settings import API_BASE_URL
from datetime import datetime

class CoinCapClient:
    """
    Cliente para consumir dados da API CoinCap.
    """
    def __init__(self):
        self.base_url = API_BASE_URL

    def get_assets(self, limit=10):
        """
        Busca informações das criptomoedas na API.
        """
        url = f"{self.base_url}/assets"
        params = {"limit": limit}
        print(f"Fazendo requisição para URL: {url} params={params}")
        try:
            response = requests.get(url, params=params, timeout=10)
            print(f"Status code: {response.status_code}")
            response.raise_for_status()
            return response.json()["data"]
        except requests.RequestException as e:
            print(f"Erro ao acessar CoinCap API: {e}")
            return []

    def prepare_crypto_data(self, assets):
        """
        Prepara os dados da API para o formato do banco de dados.
        """
        prepared_data = []
        for asset in assets:
            prepared_data.append({
                "id": asset["id"],
                "name": asset["name"],
                "symbol": asset["symbol"],
                "rank": int(asset["rank"]),
                "priceUsd": float(asset["priceUsd"]) if asset["priceUsd"] else None,
                "marketCapUsd": float(asset["marketCapUsd"]) if asset["marketCapUsd"] else None,
                "volumeUsd24Hr": float(asset["volumeUsd24Hr"]) if asset["volumeUsd24Hr"] else None,
                "changePercent24Hr": float(asset["changePercent24Hr"]) if asset["changePercent24Hr"] else None,
                "timestamp": datetime.utcnow()
            })
        return prepared_data
