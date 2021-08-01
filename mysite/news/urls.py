from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:create_id>/', get_category, name='category')
]