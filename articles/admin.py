from django.contrib import admin

# Register your models here.
from .models import Article, Brand

admin.site.register(Article)
admin.site.register(Brand)