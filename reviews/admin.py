from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review


# Register your models here.


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'score', 'approved', 'created_on')
    list_filter = ['created_on']
    