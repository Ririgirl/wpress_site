from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news' : news,
        'title': 'Список новостей'
    }
    #print(timezone.localtime(timezone.now()))
    return render(request, template_name='news/index.html', context=context)


def get_category(request, create_id):
    news = News.objects.filter(create_id=create_id)
    category = Category.objects.get(pk=create_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    #news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


