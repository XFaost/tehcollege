from django.shortcuts import get_object_or_404

from articles.models import *
from home.services.services import *


def __get_category_name(category_id):
    """
    Отримати назву категорії

    Parameters:
        category_id: int

    Return:
        str
    """
    category = Category.objects.filter(id=category_id).first()
    if category:
        return category.name
    return "Невідома категорія"


def __get_category_articles(request_args, category_id, num_page):
    """
    Отримати:
     * статті категорії із врахуванням сторінки
     * дані для рендеру навігації між сторінками

    Parameters:
        request_args: dict
        category_id: int
        num_page: int

    Note:
        Якщо category_id == 0, то виведуться усі статті

    Return:
        dict
    """
    articles = Article.objects.all().order_by('-id')

    if category_id > 0:
        category = Category.objects.filter(id=category_id).first()
        if category:
            articles = articles.filter(tags__in=category.tags.all()).distinct()

    if articles:
        return get_paginator(request_args, articles, num_page, 10)
    return None


def __generate_category_content_by_template(category_name, articles_content):
    """
    Згенерувати заповнений шаблон для рендеру списку статей

    Parameters:
        category_name: dict
        articles_content: int

    Return:
        dict
    """
    return {'name': category_name, 'articles_content': articles_content}


def get_category_content(request, category_id, num_page):
    """
    Отримати:
     * назву категорії
     * статті категорії із врахуванням сторінки та дані для рендеру навігації між сторінками

    Parameters:
        request: HttpRequest
        category_id: int
        num_page: int

    Note:
        Якщо category_id == 0, то виведуться усі статті

    Return:
        dict
    """
    name = __get_category_name(category_id)
    request_args = get_request_args(request)
    articles = __get_category_articles(request_args, category_id, num_page)
    return __generate_category_content_by_template(name, articles)


def get_article_or_404(article_id):
    """
    Отримати статтю

    Parameters:
        article_id: int

    Note:
        При відсутності отримаємо 404

    Return:
        Article
    """
    return get_object_or_404(Article, pk=article_id)
