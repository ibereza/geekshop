from django.urls import path

import baskets.views as baskets

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>', baskets.basket_add, name='basket'),
]
