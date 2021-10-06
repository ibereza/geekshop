from django.forms import ModelForm, Textarea
from mainapp.models import ProductCategory


class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 60, 'rows': 3}),
        }
