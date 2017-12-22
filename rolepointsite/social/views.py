import json

from django.shortcuts import render
from django.template import loader

def index(request):
    data = json.load(open('exercise-data.json'))
    context = {'results': data}
    return render(request, 'social/index.html', context)
