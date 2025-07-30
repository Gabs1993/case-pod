import unittest
from unittest.mock import MagicMock
from app.controller.starwars_controller import StarWarsController
import json

class TestStarWarsController(unittest.TestCase):
    
    def setUp(self):
        self.controller = StarWarsController()
        # Mocka o service para não fazer chamadas reais
        self.controller.service = MagicMock()

    def test_handle_missing_category(self):
        event = {"queryStringParameters": {}}
        response = self.controller.handle(event)
        self.assertEqual(response["statusCode"], 400)
        body = json.loads(response["body"])
        self.assertIn("error", body)

    def test_handle_success(self):
        event = {"queryStringParameters": {"category": "people", "search": "Luke"}}
        mock_data = [{"name": "Luke Skywalker"}]
        self.controller.service.get_entities.return_value = mock_data
        
        response = self.controller.handle(event)
        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body, mock_data)

    def test_handle_exception(self):
        event = {"queryStringParameters": {"category": "people"}}
        self.controller.service.get_entities.side_effect = Exception("Erro inesperado")
        
        response = self.controller.handle(event)
        self.assertEqual(response["statusCode"], 500)
        body = json.loads(response["body"])
        self.assertIn("error", body)
        self.assertEqual(body["error"], "Erro inesperado")

    def test_search_missing_params(self):
        event = {"queryStringParameters": {"category": "people"}}
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 400)
        body = json.loads(response["body"])
        self.assertIn("error", body)

    def test_search_success(self):
        event = {"queryStringParameters": {"category": "people", "search": "Darth"}}
        mock_results = [{"name": "Darth Vader"}]
        self.controller.service.search.return_value = mock_results
        
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(body, mock_results)

    def test_search_exception(self):
        event = {"queryStringParameters": {"category": "people", "search": "Darth"}}
        self.controller.service.search.side_effect = Exception("Falha na busca")
        
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 500)
        body = json.loads(response["body"])
        self.assertIn("error", body)
        self.assertEqual(body["error"], "Falha na busca")

if __name__ == "__main__":
    unittest.main()