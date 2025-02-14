from django import forms
from .models import FurnitureItem


class FurnitureItemForm(forms.ModelForm):
    class Meta:
        model = FurnitureItem
        fields = ['title', 'condition', 'description', 'price', 'rental_price', 'available_for_rent', 'available_for_sale', 'image', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 0}),
        }
