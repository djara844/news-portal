from django.shortcuts import render

from news.models import Author, News, Category


def home(request):
    """
    Function in charge of connecting the home url with the template index.html,
        Parameters:
        None

        Return the objects of Authors actives, Categories actives and the last 3 published news actives
    """
    authors = Author.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    last_news = News.objects.filter(is_active=True).order_by("-id")[:3]
    context = {"authors": authors, "categories": categories, "last_news": last_news}
    return render(request, "index.html", context)


def categories(request, slug_category):
    """
    Function in charge of connecting the categories url with the template categories.html
        Parameters:
        slug_category: str

        Return the objects of Categories active, Category name and all news actives of category slug
    """
    category = Category.objects.filter(slug=slug_category)
    if category.exists():
        category = category.first()
        news_category = News.objects.filter(category_id=category.id, is_active=True)
        categories = Category.objects.filter(is_active=True)
        context = {
            "news_category": news_category,
            "categories": categories,
            "category_name": category,
        }
    else:
        return render(request, "404.html")

    return render(request, "categories.html", context)


def news(request, slug_category, slug_news):
    """
    Function in charge of connecting the news url with the template news.html
        Parameters:
        slug_category: str
        slug_news: str

        Returns the News objects matching the slug_news and the Category objects matching the slug_category that are active
    """
    category = Category.objects.filter(slug=slug_category)
    news_item = News.objects.filter(slug=slug_news)
    if category.exists() and news_item.exists():
        category = Category.objects.filter(slug=slug_category)
        categories = Category.objects.filter(is_active=True)
        context = {"news": news_item, "categories": categories}
    else:
        return render(request, "404.html")

    return render(request, "news.html", context)


def authores(request, slug_author):
    """
    Function in charge of connecting the authors url with the template authors.html
        Parameters:
        slug_author: str

        Return the news matching the slug_author, categories objects actives and Author object matching the slug_author
    """
    author = Author.objects.filter(slug=slug_author)
    if author.exists():
        author = author.first()
        categories = Category.objects.filter(is_active=True)
        news_for_author = News.objects.filter(author_id=author.id, is_active=True)
        context = {
            "author": author,
            "categories": categories,
            "news_for_author": news_for_author,
        }
    else:
        return render(request, "404.html")

    return render(request, "authors.html", context)
