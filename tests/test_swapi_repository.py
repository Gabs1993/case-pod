import unittest
from unittest.mock import patch
from app.repositories.swapi_repository import SWAPIRepository  # Certo aqui também

class TestSWAPIRepository(unittest.TestCase):

    @patch("app.repositories.swapi_repository.requests.get")
    def test_get_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [{"name": "Luke Skywalker"}]
        }

        repo = SWAPIRepository()
        result = repo.get_data("people")

        self.assertEqual(result, [{"name": "Luke Skywalker"}])
        mock_get.assert_called_once()

    @patch("app.repositories.swapi_repository.requests.get")
    def test_get_data_error(self, mock_get):
        mock_get.side_effect = Exception("Erro de rede")

        repo = SWAPIRepository()
        result = repo.get_data("people")

        self.assertEqual(result, [])

    @patch("app.repositories.swapi_repository.requests.get")
    def test_search_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [{"name": "Darth Vader"}]
        }

        repo = SWAPIRepository()
        result = repo.search("people", "vader")

        self.assertEqual(result, [{"name": "Darth Vader"}])
        mock_get.assert_called_once()

    @patch("app.repositories.swapi_repository.requests.get")
    def test_search_error(self, mock_get):
        mock_get.side_effect = Exception("Falha de conexão")

        repo = SWAPIRepository()
        result = repo.search("people", "vader")

        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()