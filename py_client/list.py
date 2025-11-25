import requests
from getpass import getpass

# endpoint = 'http://localhost:8000/api/products/'

# get_response = requests.get(endpoint)
# print(get_response.json())

# Token Authentication

auth_endpoint = 'http://localhost:8000/api/auth/'
username = input("What's your username?\n")
password = getpass("What's your password?\n")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }
    endpoint = 'http://localhost:8000/api/products/'
    get_response = requests.get(endpoint, headers=headers)

    try:
        print(get_response.json())
    except Exception:
        print(get_response.text)
