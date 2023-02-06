from django.urls import path
from car.views import create_car, show_car, contact, error_login, thanks, update_car, eliminate_car

urlpatterns = [
    path('create_car/', create_car),
    path('show_car/', show_car, name='show_car'),
    path('contact/', contact),
    path('error_login/', error_login),
    path('thanks/', thanks),
    path('update_car/<id>/', update_car, name='update_car'),
    path('eliminate_car/<id>/', eliminate_car, name='eliminate_car'),
    ]