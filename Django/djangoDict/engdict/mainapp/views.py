import requests
import json
from django.shortcuts import render, redirect


def dictionaryFunction(word):
    main_url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'
    app_id = '503c5a03'
    app_key = '15e10deedead7d39ee1e77e668217ea8'
    language = 'en-gb'
    simplified_URL = main_url + language + '/' + str(word).lower()
    main_content = requests.get(simplified_URL, headers={'app_id': app_id, 'app_key': app_key})
    main_text = json.loads(main_content.text)
    return main_text


# Create your views here.
def home(request, *args, **kwargs):
    context = {'title': 'Home'}
    if request.method == 'POST' and request.POST.get('search') != '':
        context = {'title': 'Define', 'definition': dictionaryFunction(request.POST.get('search'))['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]}
    
    return render(request, 'mainapp/home.html', context)


