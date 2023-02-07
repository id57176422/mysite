from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm): #클래스 상속
    email = forms.EmailField(label="이메일")
    name = forms.CharField(max_length=20)
    password = forms.PasswordInput()
    Sex = forms.CharField(max_length=5)
    phone = forms.TextInput()
    address = forms.TextInput()
    class Meta:   #내부 클래스 반드시 포함
        model = User
        fields = ("username", "email", 'password1', 'password2')
