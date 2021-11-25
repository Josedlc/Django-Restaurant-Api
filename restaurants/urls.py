from django.urls import path, include
from rest_framework import routers  
from .views import *
# import everything from views
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'restaurant_types', Restaurant_typesViewSet)
router.register(r'direction', DirectionViewSet)
router.register(r'', RestaurantViewSet)

# URLS
urlpatterns = [
    path('', include(router.urls)),
    #path('view', RestaurantViewSet.as_view()),
]