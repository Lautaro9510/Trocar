from django.urls import path
from car.views import create_car

urlpatterns = [
    path('create_car/', create_car),
    ]