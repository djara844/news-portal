from django.shortcuts import render

from news.models import Author, News, Category

# Create your views here.
def home(request):
    authors = Author.objects.all()
    return render(request, "index.html", {"authors": authors})
