from django.db import models

# Create your models here.
class Products(models.Model):
    product = models.CharField(max_length=100)
    car = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    wishlist = models.BooleanField(default=False)
    wquantity = models.PositiveIntegerField(null=True)
    photo = models.ImageField(upload_to='images/', null=True)



