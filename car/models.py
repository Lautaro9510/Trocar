from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=50)
    plate=models.CharField(max_length=7)
    year=models.IntegerField()
    km=models.IntegerField(default=0)
    price=models.IntegerField()
    contact=models.EmailField()
    contact_name=models.CharField(max_length=50)
    in_house = models.BooleanField(default=True)
    image = models.ImageField(upload_to='car_image', null=False)
