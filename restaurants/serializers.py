from rest_framework import serializers

from .models import Restaurant, Direction, Restaurant_types
  
# import local data
class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direction
        fields = ('id', 'city', 'pc', 'street', 'int_number', 'ext_number', 'state', 'location') 


class Restaurant_typesSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Restaurant_types
        fields=('id', 'description')


class RestaurantSerializer(serializers.ModelSerializer):

    direction = DirectionSerializer()
    restaurant_type = Restaurant_typesSerializer()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'schedule_open', 'schedule_open', 'direction', 'phone_number', 'restaurant_type')