import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbing.org/anything'
# endpoint = 'https://httpbing.org/anything'
endpoint = 'http://localhost:8000/api/'


get_response = requests.get(endpoint)  # HTTP Request
# get_response = requests.get(endpoint, json={'query:"Hello world"'})  # HTTP Request
print(get_response.text)  # Print raw text response
print(get_response.status_code)
print(get_response.json()['message'])


"""
HTTP Request => HTML
REST API HTTP Request => JSON
JavaScript Object Notation ~ Python Dict
"""

