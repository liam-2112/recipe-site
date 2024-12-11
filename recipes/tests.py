from django.test import TestCase
from django.urls import reverse
from .models import MenuSection, MenuItem

# Create your tests here.

class TestMenuView(TestCase):

    def setUp(self):
        self.menu_section = MenuSection.objects.create(title="Rice Dishes")
        
        self.menu_item = MenuItem(section=self.menu_section,
            title="Red Rice",  ingredients="Rice, onions and chicken", description="Middle eastern food")
        self.menu_item.save()