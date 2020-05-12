from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = User.username, null = True)
    img = models.ImageField(upload_to='pics')
    ingredients = models.TextField()
    cookingDirections = models.TextField()

    def __str__(self):
        return self.name + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('index') 
        