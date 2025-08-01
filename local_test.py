from app.config.lambda_handler import lambda_handler

def test_lambda(category, search_term):
    event = {
        "path": "/search", 
        "httpMethod": "GET",  
        "queryStringParameters": {
            "category": category,
            "search": search_term
        }
    }
    context = {}
    response = lambda_handler(event, context)
    print("Status Code:", response['statusCode'])
    print("Body:")
    print(response['body'])

# Testar personagem
print("🔎 Testando busca de personagem...")
test_lambda("people", "Luke Skywalker",)

# # Testar filme
# print("\n🎬 Testando busca de filme...")
# test_lambda("species", "Human")