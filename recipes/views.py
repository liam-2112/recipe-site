from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import MenuSection, MenuItem


# Create your views here.


class MenuPage(TemplateView):
    """
    Displays menu page
    """
    template_name = 'recipes/recipes.html'

def menu_view(request):
    menu_sections = MenuSection.objects.all()
    menu_items = MenuItem.objects.all().select_related('section')

    context = {
        "menu_sections" : menu_sections,
        "menu_items" : menu_items,
    }
    
    return render(request, 'recipes/recipes.html', context)

def recipe_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'recipe_detail.html', {'item': item})