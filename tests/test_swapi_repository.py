import unittest
from unittest.mock import patch, Mock
from app.repositories.swapi_repository import SWAPIRepository 

class TestSWAPIRepository(unittest.TestCase):

    @patch("app.repositories.swapi_repository.requests.get")
    def test_get_data_people_with_enrichment(self, mock_get):
        def mocked_requests_get(url, *args, **kwargs):
            mock_resp = Mock()
            if url == "https://swapi.info/api/people/":
                mock_resp.status_code = 200
                mock_resp.json.return_value = {
                    "results": [
                        {
                            "name": "Luke Skywalker",
                            "height": "172",
                            "mass": "77",
                            "hair_color": "blond",
                            "skin_color": "fair",
                            "eye_color": "blue",
                            "birth_year": "19BBY",
                            "gender": "male",
                            "homeworld": "https://swapi.info/api/planets/1",
                            "films": [
                                "https://swapi.info/api/films/1",
                                "https://swapi.info/api/films/2",
                                "https://swapi.info/api/films/3",
                                "https://swapi.info/api/films/6"
                            ],
                            "species": [],
                            "vehicles": [
                                "https://swapi.info/api/vehicles/14",
                                "https://swapi.info/api/vehicles/30"
                            ],
                            "starships": [
                                "https://swapi.info/api/starships/12",
                                "https://swapi.info/api/starships/22"
                            ],
                            "created": "2014-12-09T13:50:51.644000Z",
                            "edited": "2014-12-20T21:17:56.891000Z",
                            "url": "https://swapi.info/api/people/1"
                        }
                    ]
                }
            elif url == "https://swapi.info/api/planets/1":
                mock_resp.status_code = 200
                mock_resp.json.return_value = {"name": "Tatooine"}
            elif url.startswith("https://swapi.info/api/films/"):
                film_data = {
                    "1": {
                        "title": "A New Hope",
                        "opening_crawl": "It is a period of civil war...",
                        "release_date": "1977-05-25",
                        "director": "George Lucas",
                        "producer": "Gary Kurtz, Rick McCallum"
                    },
                    "2": {
                        "title": "The Empire Strikes Back",
                        "opening_crawl": "It is a dark time for the Rebellion...",
                        "release_date": "1980-05-17",
                        "director": "Irvin Kershner",
                        "producer": "Gary Kurtz, Rick McCallum"
                    },
                    "3": {
                        "title": "Return of the Jedi",
                        "opening_crawl": "Luke Skywalker has returned...",
                        "release_date": "1983-05-25",
                        "director": "Richard Marquand",
                        "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum"
                    },
                    "6": {
                        "title": "Revenge of the Sith",
                        "opening_crawl": "War! The Republic is crumbling...",
                        "release_date": "2005-05-19",
                        "director": "George Lucas",
                        "producer": "Rick McCallum"
                    }
                }
                film_id = url.split("/")[-1]
                mock_resp.status_code = 200
                mock_resp.json.return_value = film_data.get(film_id, {})
            else:
                mock_resp.status_code = 404
                mock_resp.json.return_value = {}

            return mock_resp

        mock_get.side_effect = mocked_requests_get

        repo = SWAPIRepository()
        result = repo.get_data("people", "Luke Skywalker")

        self.assertEqual(result[0]["name"], "Luke Skywalker")
        self.assertEqual(result[0]["homeworld"], "Tatooine")
        self.assertEqual(len(result[0]["films"]), 4)
        self.assertIn("title", result[0]["films"][0])

        # Verificar que campos indesejados foram removidos
        for unwanted in ["created", "edited", "url", "species", "vehicles", "starships"]:
            self.assertNotIn(unwanted, result[0])

    @patch("app.repositories.swapi_repository.requests.get")
    def test_get_data_films_with_enrichment(self, mock_get):
        def mocked_requests_get(url, *args, **kwargs):
            mock_resp = Mock()
            if url == "https://swapi.info/api/films/":
                mock_resp.status_code = 200
                mock_resp.json.return_value = [
                    {
                        "title": "A New Hope",
                        "episode_id": 4,
                        "opening_crawl": "It is a period of civil war...",
                        "director": "George Lucas",
                        "producer": "Gary Kurtz, Rick McCallum",
                        "release_date": "1977-05-25",
                        "characters": [
                            "https://swapi.info/api/people/1",
                            "https://swapi.info/api/people/2",
                            "https://swapi.info/api/people/3"
                        ],
                        "planets": ["https://swapi.info/api/planets/1"],
                        "starships": ["https://swapi.info/api/starships/2"],
                        "vehicles": ["https://swapi.info/api/vehicles/4"],
                        "species": ["https://swapi.info/api/species/1"],
                        "created": "2014-12-10T14:23:31.880000Z",
                        "edited": "2014-12-20T19:49:45.256000Z",
                        "url": "https://swapi.info/api/films/1"
                    }
                ]
            elif url.startswith("https://swapi.info/api/people/"):
                id = url.split("/")[-1]
                people_names = {
                    "1": "Luke Skywalker",
                    "2": "C-3PO",
                    "3": "R2-D2"
                }
                mock_resp.status_code = 200
                mock_resp.json.return_value = {"name": people_names.get(id, f"Person {id}")}
            else:
                mock_resp.status_code = 200
                mock_resp.json.return_value = {}
            return mock_resp

        mock_get.side_effect = mocked_requests_get

        repo = SWAPIRepository()
        result = repo.get_data("films", "A New Hope")

        self.assertEqual(len(result), 1)
        film = result[0]
        self.assertEqual(film["title"], "A New Hope")
        self.assertIn("director", film)
        self.assertIn("characters", film)

        # Verificar remoção de campos indesejados
        for unwanted in ["planets","starships","vehicles","species","created","edited","url"]:
            self.assertNotIn(unwanted, film)

    @patch("app.repositories.swapi_repository.requests.get")
    def test_get_data_planets_with_enrichment(self, mock_get):
        def mocked_requests_get(url, *args, **kwargs):
            mock_resp = Mock()
            
            if url == "https://swapi.info/api/planets/":
                mock_resp.status_code = 200
                mock_resp.json.return_value = {
                    "results": [
                        {
                            "name": "Tatooine",
                            "rotation_period": "23",
                            "orbital_period": "304",
                            "diameter": "10465",
                            "climate": "arid",
                            "gravity": "1 standard",
                            "terrain": "desert",
                            "surface_water": "1",
                            "population": "200000",
                            "residents": [
                                "https://swapi.info/api/people/1",
                                "https://swapi.info/api/people/2",
                                "https://swapi.info/api/people/4"
                            ],
                            "films": [
                                "https://swapi.info/api/films/1",
                                "https://swapi.info/api/films/3"
                            ],
                            "created": "2014-12-09T13:50:49.641000Z",
                            "edited": "2014-12-20T20:58:18.411000Z",
                            "url": "https://swapi.info/api/planets/1"
                        }
                    ]
                }
            
            elif url.startswith("https://swapi.info/api/people/"):
                id = url.split("/")[-1]
                people_names = {
                    "1": "Luke Skywalker",
                    "2": "C-3PO",
                    "4": "Darth Vader"
                }
                mock_resp.status_code = 200
                mock_resp.json.return_value = {"name": people_names.get(id, f"Person {id}")}
            
            elif url.startswith("https://swapi.info/api/films/"):
                id = url.split("/")[-1]
                film_titles = {
                    "1": "A New Hope",
                    "3": "Return of the Jedi"
                }
                mock_resp.status_code = 200
                mock_resp.json.return_value = {"title": film_titles.get(id, f"Film {id}")}
            
            else:
                mock_resp.status_code = 404
                mock_resp.json.return_value = {}

            return mock_resp

        mock_get.side_effect = mocked_requests_get

        repo = SWAPIRepository()
        result = repo.get_data("planets", "Tatooine")

        self.assertEqual(len(result), 1)
        planet = result[0]
        self.assertEqual(planet["name"], "Tatooine")
        self.assertEqual(planet["rotation_period"], "23")
        self.assertEqual(planet["climate"], "arid")
        self.assertIn("Luke Skywalker", planet["residents"])
        self.assertIn("A New Hope", planet["films"])

        # Verificar que a url foi removida
        self.assertNotIn("url", planet)

if __name__ == "__main__":
    unittest.main()