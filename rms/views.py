from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from .models import *
from .serializers import CategorySerializer, FoodSerializer, TableSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class CategoryAPIView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destory(self, request, pk):
        category = Category.objects.get(id = pk)
        count = OrderItems.objects.filter(food__category = category).count()
        if count > 0:
            return Response({
                "detail" : "OrderItem with this category exist. This category cannot be deleted."
            })
        category.delete()
        return Response({
            "detail" : "The category has been deleted."
        }, status=status.HTTP_204_NO_CONTENT)

class FoodViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Food.objects.select_related().all()
    # queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class TableViewset(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class OrderViewset(ModelViewSet):
    queryset = Order.objects.prefetch_related('items').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


# class CategoryList(APIView):
    
#     def get(self, request):
#         # load data from database
#         category = Category.objects.all()
#         # convert the data into JSON
#         serializer = CategorySerializer(category, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         # load data from JSON
#         serializer = CategorySerializer(data = request.data)
#         # convert the data into Object
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "detail": "New Category Created."
#         }, status=status.HTTP_201_CREATED)

        
# class CategoryDetail(APIView):

#     def get(self, request, id):
#         # load data from the database with id
#         single_data = Category.objects.get(id=id)
#         # convert the obj into JSON
#         serializer = CategorySerializer(single_data)
#         # send the JSON
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         category = Category.objects.get(id = id)
#         count = OrderItems.objects.filter(food__category = category).count()
#         if count > 0:
#             return Response({
#                 "detail" : "OrderItem with this category exist. This category cannot be deleted."
#             })
#         category.delete()
#         return Response({
#             "detail" : "The category has been deleted."
#         }, status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, id):
#         # convert the JSON into obj
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(category, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "detail": "Category Update Successful."
#         }, status=status.HTTP_202_ACCEPTED)
    
#     def patch(self, request, id):
#          # convert the JSON into obj
#         category = Category.objects.get(id = id)
#         serializer = CategorySerializer(category, data = request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "detail": "Category Update Successful."
#         })
