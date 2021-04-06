from django.shortcuts import render

from articles.services import *


def category_view(request):
    """Відобразити статті по даній категорії"""

    if request.method == 'GET':
        category_id = get_request_int_arg(request, 'id', 0)
        category_page = get_request_int_arg(request, 'page', 1)

        args = get_base_args()
        args['category'] = get_category_content(request, category_id, category_page)
        return render(request, 'articles/category/view.html', args)


def article_view(request):
    """Відобразити статтю по її id"""

    if request.method == 'GET':
        article_id = get_request_int_arg(request, 'id', 0)

        args = get_base_args()
        args['article'] = get_article_or_404(article_id)
        return render(request, 'articles/view.html', args)
