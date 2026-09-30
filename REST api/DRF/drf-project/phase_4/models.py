from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)