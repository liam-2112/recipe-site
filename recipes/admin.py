from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MenuItem

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('title', 'ingredients', 'instructions', 'created_on')
    search_fields = ['title', 'ingredients']
    list_filter = ['created_on']