from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='recipes'),
    path('recipe/<int:item_id>/', views.recipe_detail, name='recipe_detail'),
]