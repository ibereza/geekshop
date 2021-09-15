from datetime import datetime

from django.shortcuts import render


def index(request):
    content = {
        'title': 'GeekShop',
        'datetime': datetime.now()
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'GeekShop - Каталог',
        'datetime': datetime.now()
    }
    return render(request, 'mainapp/products.html', content)
