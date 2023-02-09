from django.contrib import admin
from .models import Answer

from .models import Question
# Register your models here.
# [검색] 기능 소스 추가
# 클래스 상속이다.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)