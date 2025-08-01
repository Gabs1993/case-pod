import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from app.interfaces.repository_interface import IRepository
import re

class SWAPIRepository(IRepository):
    BASE_URL = "https://swapi.info/api/"

    def get_data(self, category: str, search: str = None) -> list:
        url = f"{self.BASE_URL}{category}/"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Erro ao acessar a API: {response.status_code}")

        json_data = response.json()
        if isinstance(json_data, dict):
            data = json_data.get("results", [])
        elif isinstance(json_data, list):
            data = json_data
        else:
            raise Exception("Formato de resposta inesperado da API.")

        # Filtro manual
        if search:
            pattern = re.compile(re.escape(search), re.IGNORECASE)
            data = [
                item for item in data
                if pattern.search(item.get("name", "")) or pattern.search(item.get("title", ""))
            ]

        # Enriquecer os dados conforme a categoria
        for item in data:
            if category == "people":
                self._enrich_with_homeworld(item)
                self._enrich_with_films(item)
            elif category == "films":
                self._enrich_with_characters(item)
            elif category == "planets":
                self._enrich_with_residents(item)
                self._enrich_with_film_names(item)
            elif category == "species":
                self._enrich_with_homeworld(item)
                self._enrich_with_people(item)
            elif category == "vehicles":
                self._enrich_with_film_names(item)
            elif category == "starships":
                self._enrich_with_film_names(item)

        return data
    
    def _fetch(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except:
            return None
    
    def _enrich_with_homeworld(self, item):
        homeworld_url = item.get("homeworld")
        if homeworld_url:
            planet_data = self._fetch(homeworld_url)
            if planet_data:
                item["homeworld"] = planet_data.get("name")

    def _enrich_with_films(self, item):
        film_urls = item.get("films", [])
        item["films"] = self._extract_film_details(film_urls)

    def _enrich_with_film_names(self, item):
        film_urls = item.get("films", [])
        film_names = []
        for url in film_urls:
            film = self._fetch(url)
            if film:
                film_names.append(film.get("title"))
        item["films"] = film_names

    def _enrich_with_characters(self, item):
        character_urls = item.get("characters", [])
        names = []
        for url in character_urls:
            person = self._fetch(url)
            if person:
                names.append(person.get("name"))
        item["characters"] = names

    def _enrich_with_residents(self, item):
        resident_urls = item.get("residents", [])
        names = []
        for url in resident_urls:
            resident = self._fetch(url)
            if resident:
                names.append(resident.get("name"))
        item["residents"] = names

    def _enrich_with_people(self, item):
        people_urls = item.get("people", [])
        names = []
        for url in people_urls:
            person = self._fetch(url)
            if person:
                names.append(person.get("name"))
        item["people"] = names

    def _extract_film_details(self, film_urls):
        enriched = []
        for url in film_urls:
            film = self._fetch(url)
            if film:
                enriched.append({
                    "title": film.get("title"),
                    "opening_crawl": film.get("opening_crawl"),
                    "release_date": film.get("release_date"),
                    "director": film.get("director"),
                    "producer": film.get("producer")
                })
        return enriched