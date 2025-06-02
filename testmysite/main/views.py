from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    contex = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_auntification': False
    }

    return render(request, 'main/index.html', contex)


def about(request):
    return HttpResponse("About")
