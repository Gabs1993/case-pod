import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from app.interfaces.repository_interface import IRepository

class SWAPIRepository(IRepository):
    BASE_URL = "https://swapi.dev/api/"

    def get_data(self, category: str, search: str = None) -> list:
        try:
            url = f"{self.BASE_URL}{category}/"
            params = {}
            if search:
                params["search"] = search

            response = requests.get(url, params=params, verify=False, timeout=5)
            response.raise_for_status()
            return response.json().get("results", [])
        except Exception as e:
            print(f"[ERROR] get_data failed: {e}")
            return []

    def search(self, category, search_term):
        try:
            url = f"{self.BASE_URL}/{category}/?search={search_term}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json().get("results", [])
        except Exception as e:
            print(f"[ERROR] search failed: {e}")
            return []