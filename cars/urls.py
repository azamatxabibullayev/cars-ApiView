from django.urls import path
from .views import ListCategoryApiView, ListCarsApiView, DetailCarsApiView

urlpatterns = [
    path('category/', ListCategoryApiView.as_view(), name='category'),
    path('cars/', ListCarsApiView.as_view(), name='cars'),
    path('<int:pk>/', DetailCarsApiView.as_view(), name='cars_detail'),
]
