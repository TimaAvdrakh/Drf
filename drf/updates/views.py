from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from django.views.generic import View
import json
from .models import Updates

def json_example(request):
    data = {
        "count": 1000,
        "content": "someContent"
    }

    json_data = json.dumps(data)

    return HttpResponse(json_data, content_type = 'application/json')

class JsonCBV(View):
    def get(self, request, *args , **kwargs):
        data = {
            "count": 1000,
            "content": "someContent"}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')

