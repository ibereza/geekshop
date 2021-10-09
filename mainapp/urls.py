from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:category_id>/', mainapp.products, name='category'),
    path('page/<int:page_id>/', mainapp.products, name='page'),
]
