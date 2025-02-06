from django import forms
from .models import MenuItem

class RecipeForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'ingredients', 'instructions', 'image',]
