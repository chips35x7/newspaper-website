from django.contrib import admin
from django.contrib.admin import ModelAdmin 



from .models import Article

class ArticleAdmin(ModelAdmin):
    list_display = [
        'title',
        'body',
        'author',
    ]

admin.site.register(Article, ArticleAdmin)