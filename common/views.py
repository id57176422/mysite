from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.

def signup(request):
    """
    회원가입
    """
    if request.method == "POST":   #클라이언트에서 POST 요청
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  #유효성체크를 거친 깨끗한 변수임
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #인증을하는함수
            login(request, user)
            return redirect('main')

    else: #클라이언트에서 GET 요청
        form = UserForm()
    return render(request, 'common/signup.html', {'form' : form})
