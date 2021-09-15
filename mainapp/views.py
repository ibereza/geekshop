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
        'datetime': datetime.now(),
        'cards': [
            {
                'img': 'vendor/img/products/Adidas-hoodie.png',
                'title': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00',
                'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'img': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'title': 'Синяя куртка The North Face',
                'price': '23 725,00',
                'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00',
                'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
            {
                'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'title': 'Черный рюкзак Nike Heritage',
                'price': '2 340,00',
                'text': 'Плотная ткань. Легкий материал.'
            },
            {
                'img': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13 590,00',
                'text': 'Гладкий кожаный верх. Натуральный материал.'
            },
            {
                'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2 890,00',
                'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
            }
        ]
    }
    return render(request, 'mainapp/products.html', content)
