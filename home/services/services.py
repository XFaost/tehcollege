from django.core.paginator import Paginator

from navigation.services import *
from home.services.request import *


def get_home_category_id():
    """
    Отримати ідентифікатор категорії статей для домашньої сторінки

    Note:
        0 - відобразити усі статті

    Return:
          int
    """
    return 0


def get_base_args():
    """
    Отримати базові аргументи для рендеру сторінки

    Return:
          dict
    """
    return {
        'navigation': get_navigation(),
        'college': {
            'fullname': 'Відокремлений структурний підрозділ "Рівненський технічний фаховий коледж Національного '
                        'університету водного господарства та природокористування"',
            'short_name': 'ВСП "Рівненський технічний фаховий коледж НУВГП"'
        }
    }


def generate_pages_list(request_args, num_page, last_page):
    """
    Отримати список сторінок

    Parameters:
        request_args: dict
        num_page: int
        last_page: int

    Return:
        list
    """

    MAX_NUM = 7
    pages_list = []

    start_list = num_page - int(MAX_NUM / 2)
    end_list = num_page + int(MAX_NUM / 2)

    if num_page < last_page / 2:
        if start_list < 1:
            end_list += abs(start_list) + 1
            start_list = 1
        if end_list > last_page:
            end_list = last_page
    else:
        if end_list > last_page:
            start_list -= end_list - last_page
            end_list = last_page
        if start_list < 1:
            start_list = 1

    for num_page in range(start_list, end_list + 1):
        args_for_url = generate_url_args_with_changes(request_args, {'page': num_page})
        pages_list.append({
            'num': num_page,
            'url': args_for_url
        })

    return pages_list


def get_paginator(request_args, items, num_page, max_quantity):
    """
    Отримати:
        * QuerySet список враховуючи сторінку
        * Дані для рендеру панелі зі сторінками

    Parameters:
        request_args: dict
        items: QuerySet
        num_page: int
        max_quantity: int

    Return:
        dict
    """

    paginator = Paginator(items, max_quantity)

    if num_page > paginator.num_pages:
        num_page = paginator.num_pages

    return {
        'items': paginator.page(num_page),
        'first_page_url': generate_url_args_with_changes(request_args, {'page': 1}),
        'num_page': num_page,
        'list_pages': generate_pages_list(request_args, num_page, paginator.num_pages),
        'last_page_url': generate_url_args_with_changes(request_args, {'page': paginator.num_pages}),
    }
