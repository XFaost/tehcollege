from articles.models import *

def get_articles():
    """Отримати статі"""
    return Article.objects.filter()

def get_article(article_id):
    """Отримати статтю по її id"""
    return Article.objects.filter(id=article_id).first()