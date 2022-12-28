from django.shortcuts import render, HttpResponse

from news.models import Author, News, Category

# Create your views here.
def home(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.filter().order_by('-id')[:3]
    context = {"authors": authors, "categories": categories, "last_news": last_news}
    return render(request, "index.html", context)

def categories(request, slug_category):
    category = Category.objects.filter(slug=slug_category)
    if category.exists():
        category = category.first()
        news_category = News.objects.filter(category_id = category.id)
        context = {"news_category": news_category}
    else:
        return render(request, "404.html")

    return render(request, "categories.html", context)

def news(request, slug_category, slug_news ):
    category = Category.objects.filter(slug=slug_category)
    news_item = News.objects.filter(slug=slug_news)
    if category.exists() and news_item.exists():
        context = {"news": news_item}
    else:
        return render(request, "404.html")

    return render(request, "news.html", context)

def authores(request, slug_author):
    author = Author.objects.filter(slug=slug_author)
    if author.exists():
        author = author.first()
        context = {"author": author}
    else:
        return render(request, "404.html")

    return render(request, "authors.html", context)
