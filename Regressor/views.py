from django.shortcuts import render

from django.http import HttpRequest

from django.http import HttpResponse
from Regressor.utils import GraphGenerator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def request_graph(x, y):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['json'] = { 'x': x, 'y':y }
    return graph(request)

@csrf_exempt
def graph(request):
    if not 'json' in request.POST:
        return HttpResponse('There is no json object in POST.')
    # request = json.loads(request.POST['json'])
    request = request.POST['json']
    if not 'x' in request or not 'y' in request:
        return HttpResponse('There is no x or y in GET when making a graph.')
    gg = GraphGenerator()
    buffer = gg.plot(request['x'], request['y'])
    response = HttpResponse(buffer.getvalue(), content_type="image/png")
    return response

def predict(request):
    pass
