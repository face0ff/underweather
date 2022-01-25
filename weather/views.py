from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("чтото там такое про погоду")

def reklama(request,rekid):
    return HttpResponse(f"<h1>попробуйте угадать что тут у нас, правельно реклама номер- <p>{rekid}</p></h1>")
