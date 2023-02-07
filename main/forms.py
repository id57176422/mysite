from django import forms
from django.contrib.auth.models import User
from .models import User


#class PostSearchForm(forms.Form):
    #search_word = forms.CharField(label='Search Word')

#class UserInfoForm(forms.ModelForm):
    #class Meta:
     #   model = User
     #   fields =['name','email', 'password']
    #    widgets = {
     #       'name' : forms.TextInput(attrs={
      #          'class' : "form-control",
      #          'style' : "max-width: 300px",
      #          'placeholder' : '아이디 입력'
        #    }),
      #      'email' : forms.EmailInput(attrs={
      #          'class' : "form-control",
     #           'style' : 'max-width: 300px',
    #            'placeholder' : '이메일'
      #      }),
      #      'password' : forms.PasswordInput(attrs={
        #        'class' : "forms-control",
      #          'style' : 'max-width:200px',
           #     'placeholder' : '비밀번호 입력'
    #        }),
      #  }
    #    def __int__(self, *args, **kwargs):
     #       super(UserInfoForm,self).__init__(*args, **kwargs)
    #        self.fields['name'].widget.attrs['maxlength'] = 5
    #        self.fields['password'].widget.attrs['maxlength'] = 12
