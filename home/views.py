from django.shortcuts import render

from home.services.request import *
from home.services.services import *
from articles.services import *


def home_view(request):
    """Відобразити головну сторінку сайту"""

    page = get_request_int_arg(request, 'page', 1)
    home_category_id = get_home_category_id()

    args = get_base_args()
    args['category'] = get_category_content(request, home_category_id, page)
    return render(request, 'home/view.html', args)
