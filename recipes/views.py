from django.shortcuts import render
from .models import Recipes

# create your views here

def recipes_list(request):
    """
    Renders the Recipes page
    """
    recipes = Recipes.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "recipes/recipes.html",
        {"recipes": recipes},
    )