import requests

headers = {'Authorization': 'Bearer 4c9c626a53d0db4c298a2bef328a0fad9f7b0a5a'}
endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'This field is done',
    'price': 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
