from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    description = models.CharField(max_length=150)
    img = models.CharField(max_length=200)

    def __str__(self):
        return self.name
