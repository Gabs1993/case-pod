from app.config.lambda_handler import lambda_handler

def run_lambda_test(category, search_term):
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
run_lambda_test("people", "Luke Skywalker",)

# # Testar filme
# print("\n🎬 Testando busca de filme...")
# run_lambda_test("species", "Human")