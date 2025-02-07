from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

# Recipe List View with Pagination
def recipe_list(request):
    recipes = MenuItem.objects.all().order_by('-id')  # Latest recipes first
    paginator = Paginator(recipes, 8)               # 8 recipes per page
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
            recipe = form.save(commit=False)
            recipe.owner = request.user  # Assigning ownership
            recipe.save()
            messages.success(request, 'Recipe added successfully! 🎉')
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

# Edit existing recipe (Authenticated Users Only)
def edit_recipe(request, id):
    recipe = get_object_or_404(MenuItem, id=id)

    if recipe.owner != request.user:
        return HttpResponseForbidden("You are not allowed to edit this recipe.")
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully! 🎉')  # Success message
            return redirect('recipe_detail', item_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})


# delete existing recipe (Authenticated Users Only)
def delete_recipe(request, id):
    recipe = get_object_or_404(MenuItem, id=id)

    if recipe.owner != request.user:
        return HttpResponseForbidden("You are not allowed to delete this recipe.")
    
    if request.method == 'POST':
        recipe.delete()
        messages.warning(request, 'Recipe deleted successfully! ⚠️')
        return redirect('recipes')  # Redirect to the recipe list view
    
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})