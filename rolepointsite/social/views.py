import json

from django.shortcuts import render
from django.template import loader

def index(request):
    search_string = request.GET.get('search', '')
    data = json.load(open('exercise-data.json'))
    names = [x['name'] for x in data if search_string in x['name']]
    context = {'results': names}
    return render(request, 'social/index.html', context)
