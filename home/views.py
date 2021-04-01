from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

from home.services.services import *
from articles.services import *

def home_view(request):
    """Відобразити головну сторінку сайту"""

    page = request.GET.get('page', '')

    args = get_base_args()
    
    args['articles'] = get_articles(None, page)
    return render(request, 'articles/category/view.html', args)