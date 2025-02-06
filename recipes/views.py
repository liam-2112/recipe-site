from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required

# Recipe List View with Pagination
def recipe_list(request):
    recipes = MenuItem.objects.all().order_by('-id')  # Latest recipes first
    paginator = Paginator(recipes, 9)               # 9 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'recipes/recipes.html', {'page_obj': page_obj})

# Recipe Detail View
def recipe_detail(request, item_id):
    recipe = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Add New Recipe (Authenticated Users Only)
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def edit_recipe(request, id):
    recipe = get_object_or_404(recipe, id=id)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

def delete_recipe(request, id):
    recipe = get_object_or_404(recipe, id=id)
    
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')  # Redirect to the recipe list view
    
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})