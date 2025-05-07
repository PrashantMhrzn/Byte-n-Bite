from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', CategoryAPIView)
router.register(r'foods', FoodViewset)

urlpatterns = [
    path('category', CategoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('category/<id>', CategoryAPIView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
] + router.urls
