from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name = 'main'  #네임스페이스 추가

urlpatterns = [
    path('main/', views.main, name='main'),
]