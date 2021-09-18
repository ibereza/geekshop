# Generated by Django 3.2.7 on 2021-09-18 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, verbose_name='category_description'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='category_name'),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='product_name')),
                ('image', models.ImageField(blank=True, upload_to='product_images')),
                ('description', models.TextField(blank=True, verbose_name='product_description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='product_price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory')),
            ],
        ),
    ]
