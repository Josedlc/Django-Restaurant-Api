from django.conf import settings
from django.db import models
from restaurants.models import Restaurant
from products.models import Products
from users.models import User

# Create your models here.


class Status(models.Model):
    description = models.CharField(max_length=50)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(Products, through="ProductDetail")



class ProductDetail(models.Model):
    order= models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()