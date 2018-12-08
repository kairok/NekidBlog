from django.shortcuts import render

# Create your views here.
from .models import *


def news_list(request):
    news = News.objects.all()
    return render(request, "blog/index.html", {"news":news})