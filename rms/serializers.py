from rest_framework import serializers
from .models import Category, Food, Table, Order, OrderItems


    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    # save function works as create and update when validation is the same
    def save(self, **kwargs):
        validated_data = self.validated_data
        # both methods call the same object
        # category = Category.objects.all()
        category = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        # checking if there exists same category
        if category > 0:
            raise serializers.ValidationError({
                "detail": "Category already exists."
            }
            )
        # if not then sending the data from user to db
        category = Category(**validated_data)
        category.save()
        return category
    


class FoodSerializer(serializers.ModelSerializer):
    taxed = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source = 'category'
        )
    class Meta:
        model = Food
        fields = ['id', 'name', 'price', 'taxed', 'category_id', 'category']

    def get_taxed(self, food:Food):
        return food.price*0.15 + food.price
    
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['number', 'available']


class OrderItemSerializer(serializers.ModelSerializer):
    food_id = serializers.PrimaryKeyRelatedField(
        queryset = Food.objects.all(),
        source = 'food'
    )
    food = serializers.StringRelatedField()
    class Meta:
        model = OrderItems
        fields = ['food_id','food']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    items = OrderItemSerializer(many=True)
    status = serializers.CharField(read_only=True)
    payment_status = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ['user', 'total_price', 'status', 'payment_status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for items in items_data:
            OrderItems.objects.create(order=order, food=items['food'])
        return order


# class CategorySerializer(serializers.Serializer):
#     # what fields to convert into JSON
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()

#     # To create a data
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
    
#     # To update a data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.save()
#         return instance