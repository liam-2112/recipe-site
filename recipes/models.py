from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class MenuItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder',
                            null=True, blank=True)
    ingredients = models.TextField(max_length=5000)
    instructions = models.TextField(blank=True, null=True)
    description = models.TextField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')  # Ownership field

    def __str__(self):
        return self.title