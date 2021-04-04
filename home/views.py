from django.shortcuts import render

from home.services.services import *
from articles.services import *


def home_view(request):
    """Відобразити головну сторінку сайту"""

    page = request.GET.get('page', 1)
    home_article_category_id = get_home_article_category_id()

    args = get_base_args()
    args['article_category'] = get_article_category(home_article_category_id, page)
    return render(request, 'home/view.html', args)
