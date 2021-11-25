from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from .serializers import OrderSerializer, StatusSerializer, ProductDetailSerializer
from .models import Order, ProductDetail, Status
from users.views import verify_token

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductDetailViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer


class OrderStatusViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer