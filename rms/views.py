from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CategorySerializer, FoodSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def list_category(request):
    if request.method == 'GET':
        # load data from database
        category = Category.objects.all()
        # convert the data into JSON
        serializer = CategorySerializer(category, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # load data from JSON
        serializer = CategorySerializer(data = request.data)
        # convert the data into Object
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "New Category Created."
        })

# fetch single data
@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def category_detail(request, id):
    if request.method == 'GET':
        # load data from the database with id
        single_data = Category.objects.get(id=id)
        # convert the obj into JSON
        serializer = CategorySerializer(single_data)
        # send the JSON
        return Response(serializer.data)
    elif request.method == 'DELETE':
        category = Category.objects.get(id = id)
        count = OrderItems.objects.filter(food__category = category).count()
        if count > 0:
            return Response({
                "detail" : "OrderItem with this category exist. This category cannot be deleted."
            })
        category.delete()
        return Response({
            "detail" : "The category has been deleted."
        })
    elif request.method == 'PUT':
        # convert the JSON into obj
        category = Category.objects.get(id = id)
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "Category Update Successful."
        })
    elif request.method == 'PATCH':
        # convert the JSON into obj
        category = Category.objects.get(id = id)
        serializer = CategorySerializer(category, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "detail": "Category Update Successful."
        })

@api_view(['GET'])
def list_food(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many = True)
    return Response(serializer.data)