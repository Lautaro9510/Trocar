from django import forms
from car.models import Car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields='__all__'


class CarUpdateForm(forms.ModelForm):

    class Meta:
        model= Car
        fields= '__all__'
