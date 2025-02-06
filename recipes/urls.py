from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipe_list, name='recipes'),
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:item_id>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:id>/delete/', views.delete_recipe, name='delete_recipe'),
]
