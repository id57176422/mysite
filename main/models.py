from django.db import models

# Create your models here.
# 아이디 비밀번호 이름 성별 주민 연락처 이메일 주소
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.TextField()
    Sex = models.CharField(max_length=5)
    phone = models.TextField()
    address = models.TextField()


