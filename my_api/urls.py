from django.urls import path,include
from .import views

app_name= 'posts'

urlpatterns=[
    #path('',views.index),
    path('/get', views.get_api),
    path('/post', views.post_api),
]