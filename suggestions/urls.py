from django.urls import path
from . import views

urlpatterns = [
    path('', views.suggestion_view, name='suggestions'),
    path('suggestions/edit_suggestion/<int:suggestion_id>',
         views.suggestion_edit, name='suggestion_edit'),
    path(
        'suggestions/delete_suggestion/<int:suggestion_id>',
        views.suggestion_delete,
        name='suggestion_delete'),
]