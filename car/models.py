from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=50)
    plate=models.CharField(max_length=7)
    color=models.CharField(max_length=30)
    year=models.IntegerField(max_length=4)
    price=models.IntegerField(max_length=8)
    contact=models.EmailField()
    contact_name=models.CharField(max_length=50)

    def __str__(self):
        return self.name