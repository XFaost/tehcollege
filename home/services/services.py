from navigation.services import *

def get_base_args():
    """Отримати базові аргументи для рендеру сторінки"""
    args = {}
    args['navigation'] = get_navigation()
    return args