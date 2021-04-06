from navigation.services import *


def get_home_category_id() -> int:
    """
    Отримати ідентифікатор категорії статей для домашньої сторінки

    0 - відобразити усі статті    
    """
    return 0


def get_base_args() -> dict:
    """Отримати базові аргументи для рендеру сторінки"""
    return {
        'navigation': get_navigation(),
        'college': {
            'fullname': 'Відокремлений структурний підрозділ "Рівненський технічний фаховий коледж Національного '
                        'університету водного господарства та природокористування"',
            'short_name': 'ВСП "Рівненський технічний фаховий коледж НУВГП"'
        }
    }

