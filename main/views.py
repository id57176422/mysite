from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q
from .models import User


# Create your views here.
#def main2(request):
   # if request.method =="POST":
       # form = UserInfoForm(request.POST)
        #if form.is_valid():
          #  new_user = User.objects.create_user(**form.cleaned_data)
          #  login(request, new_user)
           # return render(request,'main/main_form.html', {'form' : UserInfoForm})
      #  else:
    #        return HttpResponse('사용자 명이 이미 존재합니다')
    #else:
       # form = UserInfoForm()
        #return render(request, 'main/main_form.html', {'form' : UserInfoForm})


def main(request):
    return render(request, 'main/main_form.html')

def product(request):
    return render(request, 'main/product.html')

def contentform(request):
    return render(request, 'main/contentform.html')

def price(request):
    return render(request, 'main/price.html')
