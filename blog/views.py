from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
import requests

# Create your views here.
#0ec7c878
#b5aeaa7dd45fa94664b6d5cfe689309c	

def index(request):
  app_id = config('APP_ID')
  app_key = config('APP_KEY')
  query = 'cheesecake'
  response = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q='+query+'&app_id='+app_id+'&app_key='+app_key)
  jsonResponse = response.json()
  recipes = jsonResponse['hits']
  return render(request, 'blog/index.html', {'recipes': recipes})

def specific(request):
  return HttpResponse("This is the specific url")

def search(request):
  if(request.method == "POST"):
    userText = request.POST.get('usertext')
    app_id = config('APP_ID')
    app_key = config('APP_KEY')
    response = requests.get('https://api.edamam.com/api/recipes/v2?type=public&q='+userText+'&app_id='+app_id+'&app_key='+app_key)
    jsonResponse = response.json()
    recipes = jsonResponse['hits']
    return render(request, 'blog/index.html', {'recipes': recipes})
  else:
    return render(request, 'blog/index.html')

def about(request):
  return render(request, 'blog/about.html')

def contact(request):
  return render(request, 'blog/contact.html')

