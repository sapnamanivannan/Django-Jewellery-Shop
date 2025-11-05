from django.forms import ModelForm
from .models import ProductImage


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['img', 'caption']