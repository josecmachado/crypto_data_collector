import requests
from config.settings import API_BASE_URL

class CoinCapClient:
    def __init__(self):
        self.base_url = API_BASE_URL

    def get_assets(self, limit=10):
        url = f"{self.base_url}/assets"
        params = {"limit": limit}
        print(f"Requesting: {url} params={params}")
        try:
            response = requests.get(url, params=params, timeout=10)
            print("STATUS CODE:", response.status_code)
            response.raise_for_status()
            return response.json()["data"]
        except requests.RequestException as e:
            print(f"Erro ao acessar CoinCap API: {e}")
            return []
