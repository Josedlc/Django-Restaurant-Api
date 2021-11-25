from django.urls import path, include
from rest_framework import routers  
from .views import *
# import everything from views
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'orderstatus', OrderStatusViewSet)
router.register(r'productdetail', ProductDetailViewSet)
router.register(r'', OrderViewSet)

# URLS
urlpatterns = [
    path('', include(router.urls)),
   # path('view', OrderViewSet.as_view()),
]