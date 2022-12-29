from django.shortcuts import render, HttpResponse

from news.models import Author, News, Category


def home(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.filter().order_by("-id")[:3]
    context = {"authors": authors, "categories": categories, "last_news": last_news}
    return render(request, "index.html", context)


def categories(request, slug_category):
    category = Category.objects.filter(slug=slug_category)
    if category.exists():
        category = category.first()
        news_category = News.objects.filter(category_id=category.id)
        categories = Category.objects.all()
        context = {"news_category": news_category, "categories": categories, "category_name": category}
    else:
        return render(request, "404.html")

    return render(request, "categories.html", context)


def news(request, slug_category, slug_news):
    category = Category.objects.filter(slug=slug_category)
    news_item = News.objects.filter(slug=slug_news)
    if category.exists() and news_item.exists():
        category = Category.objects.filter(slug=slug_category)
        categories = Category.objects.all()
        context = {"news": news_item, "categories": categories}
    else:
        return render(request, "404.html")

    return render(request, "news.html", context)


def authores(request, slug_author):
    author = Author.objects.filter(slug=slug_author)
    if author.exists():
        author = author.first()
        categories = Category.objects.all()
        news_for_author = News.objects.filter(author_id=author.id)
        context = {
            "author": author,
            "categories": categories,
            "news_for_author": news_for_author,
        }
    else:
        return render(request, "404.html")

    return render(request, "authors.html", context)
