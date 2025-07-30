from app.controller.starwars_controller import StarWarsController

controller = StarWarsController()

def lambda_handler(event, context=None):
    path = event.get("path", "")
    http_method = event.get("httpMethod", "")

    if path == "/search" and http_method == "GET":
        return controller.search(event)
    
    # você pode deixar aqui os outros mapeamentos de rota
    return {
        "statusCode": 404,
        "body": "Not Found"
    }