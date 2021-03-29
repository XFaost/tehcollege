from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

from home.services.services import *
from articles.services import *

def home_view(request):
    """Відобразити головну сторінку сайту"""

    args = get_base_args()
    
    args['articles'] = get_articles()
    return render(request, 'home/view.html', args)