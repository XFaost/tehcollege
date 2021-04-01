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

def get_articles(category_id, page_num):
    """Отримати статі по даній категорії

        category_id - якщо не вказати, то виведеться ...
        page_num - якщо не вказати, то замынеться на 1
    """

    category_id = __to_int(category_id, 0)
    page_num = __to_int(page_num, 1)

    args = {}

    articles = None

    if category_id > 0:
        category = ArticleCategory.objects.filter(id=category_id).first()
        if category:
            articles = Article.objects.filter(tags__in=category.tags.all()).distinct()
    else:
        articles = Article.objects.all()

    print(articles)

    if articles:
        args['page_num'], args['list'], args['last_page'] = __get_paginator(articles, page_num, 2)
    return args

def get_article(article_id):
    """Отримати статтю по її id"""
    return Article.objects.filter(id=article_id).first()