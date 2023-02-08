from django.shortcuts import render, redirect, get_object_or_404
from car.models import Car
from car.forms import CarForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

@permission_required('car.add_car')
def create_car(request):

    data = {
        'form': CarForm()
    }
   
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo ingresado exitósamente')

        else:
            data["form"] = form

    return render(request, 'car/create_car.html', data)

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

@login_required
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

@permission_required('car.change_car')
def update_car(request, id):
    car = get_object_or_404(Car, id=id)
    data= {
        'form': CarForm(instance=car)
    }
    if request.method == 'POST':
        form = CarForm(data=request.POST, instance=car, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos actualizados correctamente')
            return redirect(to='show_car')
        else:
            data["form"] = form
    return render(request, 'car/update_car.html', data)

@permission_required('car.delete_car')
def eliminate_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    messages.success(request, 'Vehículo eliminado')
    return redirect(to='show_car')