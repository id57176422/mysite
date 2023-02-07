from django.urls import path
from .views import *
from . import views

app_name = 'v1'  #네임스페이스 추가

urlpatterns = [
    path('', index, name='index'),
]