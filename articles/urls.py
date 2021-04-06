from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view, name='article'),
    path('category/', views.category_view, name='category'),
]