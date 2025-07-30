from app.repositories.swapi_repository import SWAPIRepository
from app.use_cases.get_starwars_data import GetStarWarsData

class StarWarsService:
    def __init__(self):
        self.use_case = GetStarWarsData(SWAPIRepository())

    def get_entities(self, category: str, search: str = None):
        return self.use_case.execute(category, search)
    
    def search(self, category, search_term):
        return self.use_case.execute(category, search_term)