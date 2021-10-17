from django.shortcuts import render
from django.http import HttpResponse
import requests

def index (request):
    return render(request, 'blog/index.html')

def specific (request):
    return HttpResponse('content')

def article(request, article_id):
    return render(request, 'blog/index.html', {'article_id': article_id})

def search(request):
    city = request.GET['city']
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city+\
          "&units=metric&appid=826893cd0161b0014171b6c6351529fa"
    response = requests.get(url)
    jsonResponse = response.json()
    description = jsonResponse['weather'][0]['description']
    icon_code = jsonResponse['weather'][0]['icon']
    image_url = "http://openweathermap.org/img/wn/"+icon_code+"@2x.png"
    # return HttpResponse(response)
    return render(request, 'blog/index.html', {'data': jsonResponse, 'description': description, 'image_icon': image_url})

# Create your views here.
