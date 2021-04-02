from navigation.services import *

def get_home_article_category_id():
    """
    Отримати ідентифікатор категорії статей для домашньої сторінки

    0 - відобразити усі статті    
    """
    return 0

def get_base_args():
    """Отримати базові аргументи для рендеру сторінки"""
    args = {}
    args['navigation'] = get_navigation()
    return args