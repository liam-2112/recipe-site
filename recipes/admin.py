from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import MenuSection, MenuItem

# Register your models here.


@admin.register(MenuSection)
class MenuSectionAdmin(SummernoteModelAdmin):

    list_display = ['title']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('title', 'ingredients', 'instructions', 'section', 'created_on')
    search_fields = ['title', 'ingredients']
    list_filter = ['section', 'created_on']