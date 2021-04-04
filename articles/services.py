from django.core.paginator import Paginator

from articles.models import *


def __get_paginator(items, page_num, quantity):
    """Отримати paginator вказавши querylist, номер сторінки та max кількість елементів на одній сторінці"""
    paginator = Paginator(items, quantity)

    if page_num > paginator.num_pages:
        page_num = paginator.num_pages
    return page_num, paginator.page(page_num), paginator.num_pages


def __to_int(value, default):
    """Перевести змінну у int, у разі невдачі - присвоїти значення default"""
    try:
        value = int(value)
    except:
        value = default
    return value


def __get_category_name(category_id):
    """Отримати ім'я категорії по даному ідентифікатору"""
    category = ArticleCategory.objects.filter(id=category_id).first()
    if category:
        return category.name
    return "Не відома категорія"


def __get_articles_by_category(category_id, page_num):
    """Отримати статі по даній категорії

        category_id - якщо не вказати, то виведеться ...
        page_num - якщо не вказати, то замынеться на 1
    """

    category_id = __to_int(category_id, 0)
    page_num = __to_int(page_num, 1)

    args = {}

    articles = Article.objects.all().order_by('-id')

    if category_id > 0:
        category = ArticleCategory.objects.filter(id=category_id).first()
        if category:
            articles = articles.filter(tags__in=category.tags.all()).distinct()

    if articles:
        args['page_num'], args['list'], args['last_page'] = __get_paginator(articles, page_num, 2)
    return args


def __create_article_category_args(name, articles):
    """Отримати заповнений шаблон для рендеру статей певної категорії"""
    article_category = {'name': name, 'articles': articles}
    return article_category


def get_article_category(article_category_id, article_category_page):
    """Отримати назву категорії та її статті"""
    name = __get_category_name(article_category_id)
    articles = __get_articles_by_category(article_category_id, article_category_page)
    article_category = __create_article_category_args(name, articles)
    return article_category


def get_article(article_id):
    """Отримати статтю по даному id"""
    return Article.objects.filter(id=article_id).first()

def get_simple_page(simple_page_id):
    """Отримати просту сторінку по даному id"""
    return SimplePage.objects.filter(id=simple_page_id).first()
