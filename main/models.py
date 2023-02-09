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

class taintain(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    maintain = models.CharField(max_length=100)

class lastup(models.Model):
    brand = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    http = models.CharField(max_length=100,null=True)
    eatday = models.CharField(max_length=100,null=True)
    cat = models.CharField(max_length=100)
    vo1 = models.CharField(max_length=100,null=True)
    vo2 = models.CharField(max_length=100,null=True)
    vo3 = models.CharField(max_length=100,null=True)
    vo4 = models.CharField(max_length=100,null=True)
    vo5 = models.CharField(max_length=100,null=True)
    vo6 = models.CharField(max_length=100,null=True)
    vo7 = models.CharField(max_length=100,null=True)
    vo8 = models.CharField(max_length=100,null=True)
    vo9 = models.CharField(max_length=100,null=True)
    vt1 = models.CharField(max_length=100,null=True)
    vt2 = models.CharField(max_length=100,null=True)
    vt3 = models.CharField(max_length=100,null=True)
    vt4 = models.CharField(max_length=100,null=True)
    vt5 = models.CharField(max_length=100,null=True)
    vt6 = models.CharField(max_length=100,null=True)
    vt7 = models.CharField(max_length=100,null=True)
    vt8 = models.CharField(max_length=100,null=True)
    vt9 = models.CharField(max_length=100,null=True)
    vp1 = models.CharField(max_length=100,null=True)
    vp2 = models.CharField(max_length=100,null=True)
    vp3 = models.CharField(max_length=100,null=True)
    vp4 = models.CharField(max_length=100,null=True)
    vp5 = models.CharField(max_length=100,null=True)
    vp6 = models.CharField(max_length=100,null=True)
    vp7 = models.CharField(max_length=100,null=True)
    vp8 = models.CharField(max_length=100,null=True)
    vp9 = models.CharField(max_length=100,null=True)
    vpsum = models.CharField(max_length=100,null=True)
    vpr1 = models.IntegerField(null=True)
    vpr2 = models.IntegerField(null=True)
    vpr3 = models.IntegerField(null=True)
    vpr4 = models.IntegerField(null=True)
    vpr5 = models.IntegerField(null=True)
    vpr6 = models.IntegerField(null=True)
    vpr7 = models.IntegerField(null=True)
    vpr8 = models.IntegerField(null=True)
    vpr9 = models.IntegerField(null=True)
    vprsum = models.IntegerField(null=True)
    vprsumr = models.IntegerField(null=True)
    vtr1 = models.IntegerField(null=True)
    vtr2 = models.IntegerField(null=True)
    vtr3 = models.IntegerField(null=True)
    vtr4 = models.IntegerField(null=True)
    vtr5 = models.IntegerField(null=True)
    vtr6 = models.IntegerField(null=True)
    vtr7 = models.IntegerField(null=True)
    vtr8 = models.IntegerField(null=True)
    vtr9 = models.IntegerField(null=True)
    vtrsum = models.IntegerField(null=True)
    vtrsumr = models.IntegerField(null=True)