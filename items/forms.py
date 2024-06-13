from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'availability', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Descripción del producto', 'rows': '5'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Precio'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Imágen'}),
            'availability': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Disponibilidad'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }
        labels = {
            'name': '',
            'description': '',
            'price': '',
            'image': '',
        }