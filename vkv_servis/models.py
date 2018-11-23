from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=200)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    photo = models.ImageField()
