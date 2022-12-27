from django.contrib import admin
from news.models import Author, Category, News

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(News)
