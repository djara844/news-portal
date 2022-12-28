from django.shortcuts import render

from news.models import Author, News, Category

# Create your views here.
def home(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.filter().order_by('-id')[:3]
    return render(request, "index.html", {"authors": authors, "categories": categories, "last_news": last_news})
