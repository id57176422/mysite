from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name = 'main'  #네임스페이스 추가

urlpatterns = [
    path('', views.main, name='main'),
    path('product', views.product, name="product"),
    path('contentform', views.contentform, name="contentform"),
    path('price', views.price, name="price"),
]