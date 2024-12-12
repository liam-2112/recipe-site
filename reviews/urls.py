from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_view, name='reviews'),
    path('reviews/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path(
        'reviews/delete_review/<int:review_id>',
        views.review_delete,
        name='review_delete'),
]