from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .serializers import RestaurantSerializer, Restaurant_typesSerializer, DirectionSerializer
from .models import Restaurant, Restaurant_types, Direction

class RestaurantViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DirectionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class Restaurant_typesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant_types.objects.all()
    serializer_class = Restaurant_typesSerializer
