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
    image = models.ImageField(default= None, upload_to='car_image')
 

    def __str__(self):
        return self.name