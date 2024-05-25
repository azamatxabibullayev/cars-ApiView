from django.shortcuts import render
from .serializers import CategoryCarsSerializer, CarsSerializer
from .models import Cars, CategoryCars
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ListCategoryApiView(APIView):
    def get(self, request):
        category = CategoryCars.objects.all()
        serializer = CategoryCarsSerializer(category, many=True)
        serializer_data = {
            'cateory': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class ListCarsApiView(APIView):
    def get(self, request):
        model = Cars.objects.all()
        serializer = CarsSerializer(model, many=True)
        serializer_data = {
            'data': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)


class DetailCarsApiView(APIView):
    def get(self, request, pk):
        model = Cars.objects.get(id=pk)
        serializer = CarsSerializer(model)
        serializer_data = {
            'data': serializer.data,
            'status': 'success',
            'status_code': status.HTTP_200_OK
        }
        return Response(serializer_data)
