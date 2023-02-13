from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Q
# from .models import User
# from .models import King
# from .models import Board
from django.core.paginator import Paginator
from .models import uptest,lastup,taintain
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt




import main.models
import csv
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
   # path = 'C:\yi\phceeeeeee.csv'
   # file = open(path)
   # reader = csv.reader(file)
   # list = []
   # for row in reader:
   #     list.append(main.models.uptest(brand=row[0], name=row[1], price=row[2], http=row[3]))
   # main.models.uptest.objects.bulk_create(list)
   page = request.GET.get('page','1')  # GET 방식으로 정보를 받아오는 데이터
   kw=request.GET.get('kw','') #검색어 .order_by('vprsumr')
   board_list = taintain.objects.order_by('-maintain')  # models.py Board 클래스의 모든 객체를 board_list에 담음
     # Paginator(분할될 객체, 페이지 당 담길 객체수)
     # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
   if kw:
       board_list=board_list.filter(
           Q(name__icontains=kw) |
           Q(maintain__icontains=kw)

           #Q(price__maintain=kw)
       ).distinct()
   paginator = Paginator(board_list, 10)
   page_obj = paginator.get_page(page)
    #pdb_list = uptest15.objects.order_by('id') #하이픈(-) 붙이면 내림차순 안 붙이면 오름차순
   context = {'p_list': page_obj, 'kw':kw}
   return render(request, 'main/contentform.html', context)


#def price(request):
    #return render(request, 'main/price.html')

def pindex(request):
   # path = 'C:\yi\phceeeeeee.csv'
   # file = open(path)
   # reader = csv.reader(file)
   # list = []
   # for row in reader:
   #     list.append(main.models.uptest(brand=row[0], name=row[1], price=row[2], http=row[3]))
   # main.models.uptest.objects.bulk_create(list)
   page = request.GET.get('page','1')  # GET 방식으로 정보를 받아오는 데이터
   kw=request.GET.get('kw','') #검색어
   ckw = request.GET.get('ckw', '')  # 검색어
   board_list = lastup.objects.all()  # models.py Board 클래스의 모든 객체를 board_list에 담음
     # Paginator(분할될 객체, 페이지 당 담길 객체수)
     # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
   if kw:
       board_list=board_list.filter(
           Q(brand__icontains=kw)|
           Q(cat__icontains=kw) |
           Q(name__icontains=kw)
       ).distinct()
   if ckw:
       board_list = board_list.filter(

           Q(cat__icontains=ckw)

       ).distinct()
   paginator = Paginator(board_list, 10)
   page_obj = paginator.get_page(page)
    #pdb_list = uptest15.objects.order_by('id') #하이픈(-) 붙이면 내림차순 안 붙이면 오름차순
   context = {'p_list': page_obj, 'kw':kw}
   return render(request, 'main/product.html', context)


def price(request):
   # path = 'C:\yi\phceeeeeee.csv'
   # file = open(path)
   # reader = csv.reader(file)
   # list = []
   # for row in reader:
   #     list.append(main.models.uptest(brand=row[0], name=row[1], price=row[2], http=row[3]))
   # main.models.uptest.objects.bulk_create(list)
   page = request.GET.get('page','1')  # GET 방식으로 정보를 받아오는 데이터
   kw=request.GET.get('kw','') #검색어
   ckw = request.GET.get('ckw', '')  # 검색어
   board_list = lastup.objects.order_by('vprsumr')  # models.py Board 클래스의 모든 객체를 board_list에 담음
     # Paginator(분할될 객체, 페이지 당 담길 객체수)

   if kw:
       board_list=board_list.filter(
           Q(vprsumr__icontains=kw)|

           Q(price__icontains=kw)
       ).distinct()
   if ckw:
       board_list = board_list.filter(

           Q(cat__icontains=ckw)

       ).distinct()
   paginator = Paginator(board_list, 10)
   page_obj = paginator.get_page(page)  # 페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
   #pdb_list = uptest15.objects.order_by('id') #하이픈(-) 붙이면 내림차순 안 붙이면 오름차순
   context = {'p_list': page_obj, 'kw':kw}
   return render(request, 'main/price.html', context)





def mypage(request):
    return render(request, 'main/mypage.html')
@login_required(login_url='common:login')
@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호 변경이 완료되었습니다.')
            return redirect('pybo:mypage')
        else:
            messages.error(request, '다시 입력해주세요.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'change_password.html', context)


def detail(request, pdb_id):
    pdetail = lastup.objects.get(id=pdb_id)
    context = {'p_list': pdetail}
    return render(request, 'main/product_detail.html', context)

    return render(request, '', context)