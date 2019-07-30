from django.contrib import admin

from .models import Blog
# 어디서 받는지가 잘못됨
# Register your models here.
admin.site.register(Blog)
