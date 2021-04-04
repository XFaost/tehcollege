from django.shortcuts import render

from home.services.services import *
from articles.services import *


def article_category_view(request):
    """Відобразити статті по даній категорії"""

    if request.method == 'GET':
        article_category_id = request.GET.get('id', 0)
        article_category_page = request.GET.get('page', 1)

        args = get_base_args()
        args['article_category'] = get_article_category(article_category_id, article_category_page)
        return render(request, 'articles/category/view.html', args)


def article_view(request):
    """Відобразити статтю по її id"""

    if request.method == 'GET':
        article_id = request.GET.get('id', 0)

        args = get_base_args()
        args['article'] = get_article_or_404(article_id)
        return render(request, 'articles/view.html', args)


def simple_page_view(request):
    """Відобразити просту сторіну по її id"""

    if request.method == 'GET':
        simple_page_id = request.GET.get('id', 0)

        args = get_base_args()
        args['simple_page'] = get_simple_page_or_404(simple_page_id)
        return render(request, 'articles/simple_page/view.html', args)
