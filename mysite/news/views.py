from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import News


def index(request):
    news = News.objects.all()
    #print(timezone.localtime(timezone.now()))
    return render(request, 'news/index.html', {'news':news, 'title':'Список новостей'})

