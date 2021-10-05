from django.contrib import admin
from .models import ProductCategory, Products

admin.site.register(ProductCategory)
# admin.site.register(Products)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('name', 'price')
    search_fields = ('name',)
