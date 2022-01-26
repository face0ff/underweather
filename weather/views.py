from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("чтото там такое про погоду")

def reklama(request,rekid):
    if rekid > 1:
        return HttpResponse(f"<h1>попробуйте угадать что тут у нас, правельно реклама номер- <p>{rekid}</p></h1>")
    else:
        return redirect('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> ничего тут нет</h1>')