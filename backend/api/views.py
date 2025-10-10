import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request => HttpRequest -> Django instance
    # request.body

    body = request.body  # byte string of JSON data
    data = {}

    try:
        data = json().loads(body)
    except:
        pass

    print(body)

    return JsonResponse({'message': 'Hi there, this is your Django API response!!'})

