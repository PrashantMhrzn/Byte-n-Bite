from django.urls import path, include
from .views import *

urlpatterns = [
    path('category', list_category),
    path('category/<id>', category_detail),
    path('food', list_food),
]
