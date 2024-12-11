from django.shortcuts import render
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