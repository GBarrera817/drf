import requests

endpoint = 'https://httpbin.org/status/200/'
endponit = 'https://httpbing.org/anything'


get_response = requests.get(endpoint)  # HTTP Request
# get_response = requests.get(endpoint, json={'query:"Hello world"'})  # HTTP Request
print(get_response.text)  # Print raw text response
print(get_response.json())
print(get_response.status_code)


"""
HTTP Request => HTML
REST API HTTP Request => JSON
JavaScript Object Notation ~ Python Dict
"""

