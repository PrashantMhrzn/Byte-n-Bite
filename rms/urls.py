from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', CategoryAPIView)
router.register(r'foods', FoodViewset)
router.register(r'table', TableViewset)

urlpatterns = [
    # path('category', CategoryAPIView.as_view({'get': 'list', 'post': 'create'})),
    # path('category/<pk>', CategoryAPIView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
    # path('food', FoodViewset.as_view({'get': 'list', 'post': 'create'})),
    # path('food/<pk>', FoodViewset.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
    # path('table', TableViewset.as_view({'get': 'list', 'post': 'create'})),
    # path('table/<pk>', TableViewset.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update', 'patch': 'partial_update'})),
] + router.urls
