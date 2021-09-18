from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='category_name', max_length=64, unique=True)
    description = models.TextField(verbose_name='category_description', blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='product_name', max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(verbose_name='product_description', blank=True)
    price = models.DecimalField(verbose_name='product_price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
