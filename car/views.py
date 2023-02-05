from django.shortcuts import render
from car.models import Car
from car.forms import CarForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def create_car(request):
    if request.method == 'GET':
        context = {
            'form': CarForm()
        }

        return render(request, 'car/create_car.html', context=context)   
    elif request.method == 'POST':
        form = CarForm(request.POST, files=request.FILES)
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
               image=form.cleaned_data['image']

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

    if request.method=='POST':

        name=request.POST["name"]

        message=request.POST["vehicle"]+" "+request.POST["email"]+" "+request.POST["phone"]+" "+request.POST["message"]

        email_from=settings.EMAIL_HOST_USER

        recipient_list=["servertestmdq@gmail.com"]

        send_mail(name, message, email_from, recipient_list)

        return render(request, 'car/thanks.html')
    
    return render(request, 'car/contact.html')

def error_login(request):

    return render(request, 'car/error_login.html')

def thanks(request):

    return render(request, 'car/thanks.html')