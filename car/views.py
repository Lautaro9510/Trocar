from django.shortcuts import render
from car.models import Car
from car.forms import CarForm

# Create your views here.

def create_car(request):
    if request.method == 'GET':
        context = {
            'form': CarForm()
        }

        return render(request, 'car/create_car.html', context=context)   
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Car.objects.create(
               name=form.cleaned_data['name'],
               plate=form.cleaned_data['plate'],
               year=form.cleaned_data['year'],
               km=form.cleaned_data['km'],
               price=form.cleaned_data['price'],
               contact=form.cleaned_data['contact'],
               contact_name=form.cleaned_data['contact_name'],
               in_house=form.cleaned_data['in_house'],

            )
            context= {
                'message': 'Vehículo ingresado exitósamente'
            }

        else:
            context= {
                'form_errors': form.errors,
                'form': CarForm()
            }
        return render(request, 'car/create_car.html', context=context)

def show_car(request):
    if 'search' in request.GET:
        search = request.GET['search']
        car = Car.objects.filter(name__ifcontains=search)
    else:
        car= Car.objects.all()
    context = {
        'car':car,
    }
    return render(request, 'car/show_car.html', context=context)

def contact(request):
    
    return render(request, 'car/contact.html', context={})