from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

# Create your views here.
def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Это наш армянский супер пупер магазин мы здесь такие все на бизнесе сидим кайфуем словно это нефтетруба а это мебель йоу'
    }

    return render(request, 'main/about.html', context)