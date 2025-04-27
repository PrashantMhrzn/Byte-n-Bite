from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer, FoodSerializer

# Create your views here.
@api_view(['GET'])
def list_category(request):
    # load data from database
    category = Category.objects.all()
    # convert the data into JSON
    serializer = CategorySerializer(category, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def list_food(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many = True)
    return Response(serializer.data)