import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request => HttpRequest -> Django instance
    # request.body

    print(request.GET) # url query params
    # print(request.POST) 

    body = request.body  # byte string of JSON data
    data = {}

    try:
        data = json.loads(body) # string of JSON data -> Python Dict

    except:

        pass

    # print(data)

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    
    print(request.headers)
    
    return JsonResponse(data)

