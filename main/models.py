from django.db import models
from django.contrib.auth.models import User
import sqlite3
# Create your models here.
# 아이디 비밀번호 이름 성별 주민 연락처 이메일 주소


 #class Usera(models.Model):
   # name = models.CharField(max_length=20)
  #  email = models.EmailField()
    #password = models.TextField()
   # Sex = models.CharField(max_length=5)
   # phone = models.TextField()
  #  address = models.TextField()











#class Board(models.Model):
 #    subject = models.CharField(max_length=200)
 #    content = models.TextField()
 #    create_date = models.DateTimeField()
   #  author = models.ForeignKey(User, on_delete=models.CASCADE)
  #   hits = models.PositiveIntegerField(default=0)
     #제목 반환
 #    def __str__(self):
  #       return self.subject
     #조회수
    # @property
   #  def update_counter(self):
    #     self.hits += 1
   #      self.save()


class King(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    http = models.CharField(max_length=100)

class uptest(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    http = models.CharField(max_length=100)