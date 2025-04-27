from django.urls import path, include
from .views import list_category, list_food

urlpatterns = [
    path('category', list_category),
    path('food', list_food),
]
