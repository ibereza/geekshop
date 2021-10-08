from django.shortcuts import render
from .models import ProductCategory, Products


def index(request):
    return render(request, 'mainapp/index.html', {'title': 'GeekShop'})


def products(request, category_id=None):
    # products_content = Products.objects.all()
    # products_content = Products.objects.filter(
    #     category_id=category_id) if category_id is not None else Products.objects.all()
    products_content = Products.objects.all() if category_id is None else Products.objects.filter(
        category_id=category_id)
    category_content = ProductCategory.objects.all()

    content = {
        'title': 'GeekShop - Каталог',
        'products': products_content,
        'categories': category_content,
    }
    return render(request, 'mainapp/products.html', content)
