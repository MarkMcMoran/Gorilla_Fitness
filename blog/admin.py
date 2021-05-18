from django.contrib import admin
from .models import News_Post, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(News_Post)