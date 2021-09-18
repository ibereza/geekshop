from datetime import datetime
import json

from django.shortcuts import render
from .models import ProductCategory, Products


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'GeekShop', 'datetime': datetime.now()})


def products(request):
    category_content = ProductCategory.objects.all()
    products_content = Products.objects.all()
    content = {
        'title': 'GeekShop - Каталог',
        'datetime': datetime.now(),
        'products': products_content,
        'categories': category_content,
    }
    return render(request, 'mainapp/products.html', content)
