from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    contex = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', contex)


def about(request):
    contex = {
        'title': 'Home - О нас',
        'content': 'Страница О нас',
        'text_on_page': "Тут будет написана вся информация о нашей компании!"
    }

    return render(request, 'main/about.html', contex)
