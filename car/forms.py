from django import forms

class CarForm(forms.Form):
    name= forms.CharField(max_length=50)
    plate= forms.CharField(max_length=7)
    year= forms.IntegerField()
    km= forms.IntegerField()
    price= forms.IntegerField()
    contact= forms.EmailField()
    contact_name= forms.CharField(max_length=50)
    in_house= forms.BooleanField(required= False)
    image = forms.ImageField()