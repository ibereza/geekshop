from datetime import datetime
import json

from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'GeekShop', 'datetime': datetime.now()})


def products(request):
    with open('mainapp/fixtu/products.json', encoding='UTF-8') as f:
        product_base = json.load(f)
    content = {
        'title': 'GeekShop - Каталог',
        'datetime': datetime.now(),
        'cards': product_base
    }
    return render(request, 'mainapp/products.html', content)
