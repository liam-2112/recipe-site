from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class MenuSection(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    section = models.ForeignKey(
        MenuSection,
        on_delete=models.CASCADE,
        related_name="section"
        )
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder',
                            null=True, blank=True)
    ingredients = models.TextField(max_length=5000)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['section']

    def __str__(self):
        return self.title