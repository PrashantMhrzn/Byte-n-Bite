from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    # what fields to convert into JSON
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    # To create a data
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    # To update a data
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    


class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()