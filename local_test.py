from app.config.lambda_handler import lambda_handler
import json

def run_lambda_test(categories, searches):
    event = {
        "path": "/search",
        "httpMethod": "GET",
        "queryStringParameters": {
            "category": json.dumps(categories),
            "search": json.dumps(searches)
        }
    }
    context = {}
    response = lambda_handler(event, context)
    print("Status Code:", response['statusCode'])
    print("Body:")
    print(response['body'])

print("🔎 Testando múltiplos parâmetros...")
run_lambda_test(["people", "films"], ["Luke Skywalker", "A New Hope"])