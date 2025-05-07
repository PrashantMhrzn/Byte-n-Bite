from rest_framework import serializers
from .models import Category, Food


    
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
        fields = ['id', 'name', 'price', 'taxed', 'category']

    def get_taxed(self, food:Food):
        return food.price*0.15 + food.price


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