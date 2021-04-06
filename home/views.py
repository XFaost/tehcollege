from django.shortcuts import render

from home.services.request import *
from home.services.services import *
from articles.services import *


def home_view(request):
    """Відобразити головну сторінку сайту"""

    page = get_int_from_request(request, 'page', 1)
    home_category_id = get_home_category_id()

    args = get_base_args()
    args['category'] = get_category(home_category_id, page)
    return render(request, 'home/view.html', args)
