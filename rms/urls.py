from django.urls import path, include
from .views import *

urlpatterns = [
    path('category', CategoryList.as_view()),
    path('category/<id>', CategoryDetail.as_view()),
    path('food', list_food),
]
