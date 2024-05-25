from rest_framework import serializers
from .models import Cars, CategoryCars


class CategoryCarsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = CategoryCars
        fields = '__all__'


class CarsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    video = serializers.FileField()
    audio = serializers.FileField()
    dock = serializers.FileField()

    class Meta:
        model = Cars
        fields = '__all__'
