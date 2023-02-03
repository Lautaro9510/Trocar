from django.urls import path
from car.views import create_car, show_car, contact, error_login

urlpatterns = [
    path('create_car/', create_car),
    path('show_car/', show_car),
    path('contact/', contact),
    path('error_login/', error_login)
    ]