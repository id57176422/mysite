from django.contrib import admin
from my_api.models import Bbs
# Register your models here.

class my_apiAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created',)

admin.site.register(Bbs, my_apiAdmin)
