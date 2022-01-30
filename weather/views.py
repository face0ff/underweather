from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from weather import rfmain
from .models import *
import requests
import datetime

# rfmain.get_weather("odesa", '1042c1a58dff11fbe074c60d79e1beac')

menu = [{'title': "Погода", 'url_name': 'home'},
        {'title':'Спа','url_name':'spa'}
        ]




def index(request):
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=odesa&APPID=1042c1a58dff11fbe074c60d79e1beac&units=metric&lang=RU"
    )
    data = r.json()
    print(data)




    mesta = Mesta.objects.all()
    context = {
        'mesta': mesta,
        'menu': menu,
        'title': 'Главная страница',
        'gorod': data['name'],
        'tempVo': data['main']['temp'],
        'feel': data['main']['feels_like'],
        'press': data['main']['pressure'],
        'windS': data['wind']['speed'],
        'windD': data['wind']['deg'],
        'sunrise': datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
        'sunset': datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
        'pogoda': data['weather'][0]['main'],
        'right_now': datetime.datetime.now().strftime('%Y-%m-%d'),
        'length_day': datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

    }
    return render(request, 'weather/index.html',  context=context,)

# def reklama(request,rekid):
#     return render(f"<h1>попробуйте угадать что тут у нас, правельно реклама номер- <p>{rekid}</p></h1>")
def spa(request):
    return render(request, 'weather/spa.html' , {'menu': menu,'title': 'SPA'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> ничего тут нет</h1>')