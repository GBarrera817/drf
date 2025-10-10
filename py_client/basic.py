import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbing.org/anything'
# endpoint = 'https://httpbing.org/anything'
endpoint = 'http://localhost:8000/api/'


# get_response = requests.get(endpoint)  # HTTP Request
payload = {'abc': 123}
get_response = requests.get(endpoint, params=payload, json={'query':'Hello world'})  # HTTP Request
# print(get_response.text)  # Print raw text response
# print(get_response.status_code)


"""
HTTP Request => HTML
REST API HTTP Request => JSON
JavaScript Object Notation ~ Python Dict
"""

print(get_response.json())
