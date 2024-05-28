from django.urls import path
from .views import ListCategoryApiView, ListCarsApiView, DetailCarsApiView, DeleteCarsView, UpdateCarsView, \
    CreateCarView

urlpatterns = [
    path('category/', ListCategoryApiView.as_view(), name='category'),
    path('cars/', ListCarsApiView.as_view(), name='cars'),
    path('cars-detail/<int:pk>', DetailCarsApiView.as_view(), name='cars_detail'),
    path('cars-delete/<int:pk>', DeleteCarsView.as_view(), name='cars_delete'),
    path('cars-update/<int:pk>', UpdateCarsView.as_view(), name='cars_update'),
    path('cars-create/', CreateCarView.as_view(), name='cars_create'),
]
