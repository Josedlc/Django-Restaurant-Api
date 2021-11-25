from rest_framework import serializers

from .models import Products
  
# import local data
class ProductsSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'img')
