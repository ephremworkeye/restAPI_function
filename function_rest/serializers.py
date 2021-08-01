from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    max_length = serializers.IntegerField()
    revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = CategorySerializer()

    