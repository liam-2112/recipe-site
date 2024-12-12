from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suggestion(models.Model):
    """
    This class represents a suggestion model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="author")
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(max_length=5000, null=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Suggestion {self.title} | {self.author} | {self.created_on}"