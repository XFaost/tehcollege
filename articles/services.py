from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from articles.models import *


def __get_paginator(items: list, page_num: int, max_quantity: int) -> dict:
    """Отримати paginator вказавши QuerySet items, номер сторінки page_num та max кількість елементів max_quantity на одній сторінці"""

    paginator = Paginator(items, max_quantity)

    if page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return {
        'page_num': page_num,
        'list': paginator.page(page_num),
        'last_page': paginator.num_pages
    }


def __get_category_name(category_id: int) -> str:
    """Отримати ім'я категорії по ідентифікатору category_id"""
    category = Category.objects.filter(id=category_id).first()
    if category:
        return category.name
    return "Не відома категорія"


def __get_articles_by_category(category_id: int, page_num: int) -> dict:
    """
    Отримати статі, які належать категорії з id=category_id на сторінці page_num

    category_id - 0, то виведуться усі статті
    """

    articles = Article.objects.all().order_by('-id')

    if category_id > 0:
        category = Category.objects.filter(id=category_id).first()
        if category:
            articles = articles.filter(tags__in=category.tags.all()).distinct()

    if articles:
        return __get_paginator(articles, page_num, 2)
    return {}


def __create_category_args(name: str, articles: list) -> dict:
    """Отримати заповнений шаблон для рендеру списку статей вказавши """
    return {'name': name, 'articles': articles}


def get_category(category_id: int, category_page: int) -> dict:
    """Отримати назву категорії та її статті"""
    name = __get_category_name(category_id)
    articles = __get_articles_by_category(category_id, category_page)
    return __create_category_args(name, articles)


def get_article_or_404(article_id: int) -> Article:
    """
    Отримати статтю з id=article_id

    При відсутності отримаємо 404    
    """
    return get_object_or_404(Article, pk=article_id)
