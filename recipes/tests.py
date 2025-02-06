from django.test import TestCase
from django.urls import reverse
from .models import MenuItem

# Create your tests here.

class TestMenuView(TestCase):

    def setUp(self):
        self.menu_item = MenuItem(
            title="Red Rice",  ingredients="Rice, onions and chicken", description="Middle eastern food")
        self.menu_item.save()