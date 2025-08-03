import unittest
from unittest.mock import MagicMock
from app.controller.starwars_controller import StarWarsController
import json

class TestStarWarsController(unittest.TestCase):
    
    def setUp(self):
        self.controller = StarWarsController()
        self.controller.service = MagicMock()

    def test_search_missing_params(self):
    # Parâmetros não passados, ou inválidos (não JSON ou listas diferentes)
        event = {"queryStringParameters": {"category": "[\"people\"]"}}
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 400)
        body = json.loads(response["body"])
        self.assertIn("error", body)

        event = {"queryStringParameters": {"category": "notjson", "search": "[\"Luke\"]"}}
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 400)

        event = {"queryStringParameters": {"category": "[\"people\"]", "search": "[\"Luke\", \"Darth\"]"}}
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 400)

    def test_search_success(self):
        event = {
            "queryStringParameters": {
                "category": "[\"people\", \"films\"]",
                "search": "[\"Luke\", \"A New Hope\"]"
            }
        }
        # Mock para cada chamada do service.search
        self.controller.service.search.side_effect = [
            [{"name": "Luke Skywalker"}],
            [{"title": "A New Hope"}]
        ]
        
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 200)
        body = json.loads(response["body"])
        self.assertEqual(len(body), 2)
        self.assertEqual(body[0], [{"name": "Luke Skywalker"}])
        self.assertEqual(body[1], [{"title": "A New Hope"}])

    def test_search_exception(self):
        event = {
            "queryStringParameters": {
                "category": "[\"people\"]",
                "search": "[\"Darth\"]"
            }
        }
        self.controller.service.search.side_effect = Exception("Falha na busca")
        
        response = self.controller.search(event)
        self.assertEqual(response["statusCode"], 500)
        body = json.loads(response["body"])
        self.assertIn("error", body)
        self.assertEqual(body["error"], "Falha na busca")

if __name__ == "__main__":
    unittest.main()