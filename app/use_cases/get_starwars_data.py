from app.interfaces.repository_interface import IRepository
from app.models.starwars_entity import StarWarsEntity

class GetStarWarsData:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def execute(self, category: str, search: str = None):
        raw_data = self.repository.get_data(category, search)
        return [StarWarsEntity(item.get("name") or item.get("title"), item).to_dict() for item in raw_data]