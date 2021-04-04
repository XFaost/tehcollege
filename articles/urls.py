from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view, name='article'),
    path('/category', views.article_category_view, name='article_category'),
    path('/simple_page', views.simple_page_view, name='simple_page')
]