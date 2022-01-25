from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('reklama/<int:rekid>/', reklama),

]