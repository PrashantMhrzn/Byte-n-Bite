from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    # what fields to convert into JSON
    id = serializers.IntegerField()
    name = serializers.CharField()

class FoodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()