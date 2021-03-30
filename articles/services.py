from django.core.paginator import Paginator

from articles.models import *

def get_articles(page_num):
    """Отримати статі"""

    args = {}

    paginator = Paginator(Article.objects.all(), 2)
    if not page_num:
        page_num = 1
    
    args['list'] = paginator.page(int(page_num))
    args['page_num'] = int(page_num)
    args['last_page'] = paginator.num_pages

    return args

def get_article(article_id):
    """Отримати статтю по її id"""
    return Article.objects.filter(id=article_id).first()