from app.interfaces.repository_interface import IRepository
from app.models.starwars_entity import StarWarsEntity

class GetStarWarsData:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def execute(self, category: str, search: str = None):
        raw_data = self.repository.get_data(category, search)
        entities = []

        for item in raw_data:
            name = item.get("name") or item.get("title")
            details = {
                k: v for k, v in item.items() if k.lower() not in ["name", "title"]
            }
            entities.append(StarWarsEntity(name, details).to_dict())

        return entities