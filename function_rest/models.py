from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

class Movie(models.Model):
    category = models.ForeignKey(Category, related_name='movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    max_length = models.PositiveIntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    
    

