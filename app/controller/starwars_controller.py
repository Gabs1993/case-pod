import json
from app.services.starwars_service import StarWarsService

class StarWarsController:
    def __init__(self):
        self.service = StarWarsService()

    def handle(self, event):
        try:
            query = event.get("queryStringParameters") or {}
            category = query.get("category")
            search = query.get("search")

            if not category:
                return self._response(400, {"error": "Missing 'category' parameter"})

            data = self.service.get_entities(category, search)
            return self._response(200, data)

        except Exception as e:
            return self._response(500, {"error": str(e)})
        
    
    def search(self, event):
        query_params = event.get("queryStringParameters") or {}

        category = query_params.get("category")
        search = query_params.get("search")

        if not category or not search:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Parâmetros 'category' e 'search' são obrigatórios"})
            }

        try:
            results = self.service.search(category, search)
            return {
                "statusCode": 200,
                "body": json.dumps(results)
            }
        except Exception as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": str(e)})
            }

    def _response(self, status_code, body):
        return {
            "statusCode": status_code,
            "body": json.dumps(body),
            "headers": {
                "Content-Type": "application/json"
            }
        }