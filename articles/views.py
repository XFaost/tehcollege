from django.shortcuts import render

from home.services.services import *
from articles.services import *


def article_category_view(request):
    """Відобразити статті по даній категорії"""

    if request.method == 'GET':
        args = get_base_args()

        article_category_id = request.GET.get('id', '')
        article_category_page = request.GET.get('page', '')

        args['article_category'] = get_article_category(article_category_id, article_category_page)
        return render(request, 'articles/category/view.html', args)


def article_view(request):
    """Відобразити статтю по її id"""

    if request.method == 'GET':
        args = get_base_args()

        article_id = request.GET.get('id', '')
        args['article'] = get_article(article_id)
        return render(request, 'articles/view.html', args)

def simple_page_view(request):
    """Відобразити просту сторіну по її id"""

    if request.method == 'GET':
        args = get_base_args()

        simple_page_id = request.GET.get('id', '')
        args['simple_page'] = get_simple_page(simple_page_id)
        return render(request, 'articles/simple_page/view.html', args)
