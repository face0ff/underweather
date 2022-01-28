from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *


from .models import *
menu = [{'title': "Погода", 'url_name': 'home'},
        {'title':'Спа','url_name':'spa'}
        ]

def index(request):
    mesta = Mesta.objects.all()
    context = {
        'mesta': mesta,
        'menu': menu,
        'title': 'Главная страница'

    }
    return render(request, 'weather/index.html', context=context)

# def reklama(request,rekid):
#     return render(f"<h1>попробуйте угадать что тут у нас, правельно реклама номер- <p>{rekid}</p></h1>")
def spa(request):
    return render(request, 'weather/spa.html' , {'menu': menu,'title': 'SPA'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> ничего тут нет</h1>')