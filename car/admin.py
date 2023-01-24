from django.contrib import admin
from car.models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'plate', 'year', 'km', 'price', 'contact', 'contact_name', 'image')
    list_filter = ('in_house',)
    search_fields = ('name',)