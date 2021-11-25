from rest_framework import serializers
from django.utils.text import gettext_lazy as _
from .models import Order, Status, ProductDetail
from restaurants.serializers import RestaurantSerializer
from products.serializers import ProductsSerializer
from users.serializers import UserSerializer
# import local data

class OrderSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    class Meta:
        model = Order
        fields = ('id', 'user', 'time', 'restaurant', 'status', 'products')

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = ('id', 'order', 'product', 'quantity')

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'description')