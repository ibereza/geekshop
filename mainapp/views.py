from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ProductCategory, Products


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'GeekShop'})


def products(request, category_id=None, page_id=1):
    products_content = Products.objects.all() if category_id is None else Products.objects.filter(
        category_id=category_id)
    category_content = ProductCategory.objects.all()

    paginator = Paginator(products_content, per_page=3)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': 'GeekShop - Каталог',
        'products': products_paginator,
        'categories': category_content,
    }
    return render(request, 'mainapp/products.html', content)
