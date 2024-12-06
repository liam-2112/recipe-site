from . import views
from django.urls import path

urlpatterns = [
    path('', views.recipes_list, name='recipes'),
]