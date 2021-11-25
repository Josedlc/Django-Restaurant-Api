from django.urls import path, include
from rest_framework import routers  
from .views import *

router = routers.DefaultRouter()

router.register(r'', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('view', ProductsViewSet.as_view()),
]