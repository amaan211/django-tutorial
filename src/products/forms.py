from django import forms

from .models import Product,Employee,Anime

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "summary",
        ]