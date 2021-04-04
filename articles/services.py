from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from articles.models import *


def __get_paginator(items: list, page_num: int, max_quantity: int) -> dict:
    """Отримати paginator вказавши querylist, номер сторінки та max кількість елементів на одній сторінці"""

    paginator = Paginator(items, max_quantity)

    if page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return {
        'page_num': page_num,
        'list': paginator.page(page_num),
        'last_page': paginator.num_pages
    }


def __get_category_name(category_id: int) -> str:
    """Отримати ім'я категорії по даному ідентифікатору"""
    category = ArticleCategory.objects.filter(id=category_id).first()
    if category:
        return category.name
    return "Не відома категорія"


def __get_articles_by_category(category_id: int, page_num: int) -> dict:
    """
    Отримати статі по даній категорії та сторінці

    category_id - 0, то виведуться усі статті
    """

    articles = Article.objects.all().order_by('-id')

    if category_id > 0:
        category = ArticleCategory.objects.filter(id=category_id).first()
        if category:
            articles = articles.filter(tags__in=category.tags.all()).distinct()

    if articles:
        return __get_paginator(articles, page_num, 2)
    return {}


def __create_article_category_args(name: str, articles: list) -> dict:
    """Отримати заповнений шаблон для рендеру списку статей"""
    return {'name': name, 'articles': articles}


def get_article_category(article_category_id: int, article_category_page: int) -> dict:
    """Отримати назву категорії та її статті"""
    name = __get_category_name(article_category_id)
    articles = __get_articles_by_category(article_category_id, article_category_page)
    return __create_article_category_args(name, articles)


def get_article_or_404(article_id: int) -> Article:
    """
    Отримати статтю по даному id

    При відсутності отримаємо 404    
    """
    return get_object_or_404(Article, pk=article_id)


def get_simple_page_or_404(simple_page_id: int) -> SimplePage:
    """
    Отримати просту сторінку по даному id

    При відсутності отримаємо 404    
    """
    return get_object_or_404(SimplePage, pk=simple_page_id)
