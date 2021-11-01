from django.db import models
from home.models import Products

# Create your models here.
class Cart(models.Model):
    pid = models.ForeignKey(Products,on_delete=models.CASCADE,null=False)
    wquantity = models.PositiveIntegerField(null=False)