from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:create_id>/', get_category, name='category'),
    # path('category/<int:create_id>/', NewsByCategory.as_view(extra_context={'title': 'Категория'}), name='category'),
    path('category/<int:create_id>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news')
    path('news/add-news/', CreateNews.as_view(), name='add_news')
]