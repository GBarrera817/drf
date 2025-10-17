import requests

endpoint = 'http://localhost:8000/api/products/123428374237942364289342936423/'

get_response = requests.get(endpoint)


print(get_response.json())
