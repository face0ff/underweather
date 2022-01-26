from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('reklama/<int:rekid>/', reklama),

]