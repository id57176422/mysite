from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hits = models.PositiveIntegerField(default=0)
    #제목 반환
    def __str__(self):
        return self.subject
    #조회수
    @property
    def update_counter(self):
        self.hits += 1
        self.save()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)