import pytest
from app.services.starwars_service import StarWarsService

# Criando uma versão falsa do repositório
class MockSWAPIRepository:
    def get_data(self, category, search=None):
        return [{"name": "Luke Skywalker"}, {"name": "Leia Organa"}]

# Criando um mock da use case que usa o repositório mockado
class MockGetStarWarsData:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, category, search=None):
        return self.repository.get_data(category, search)

# Substituindo o use case real por um mock no service
class MockStarWarsService(StarWarsService):
    def __init__(self):
        self.use_case = MockGetStarWarsData(MockSWAPIRepository())

def test_get_entities_returns_data():
    service = MockStarWarsService()
    result = service.get_entities("people")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["name"] == "Luke Skywalker"

def test_search_returns_filtered_data():
    service = MockStarWarsService()
    result = service.search("people", "Luke")

    assert isinstance(result, list)
    assert result[0]["name"] == "Luke Skywalker"