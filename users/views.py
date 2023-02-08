from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from users.models import User
from users.forms import RegisterForm, UserUpdateForm, UserProfileForm
from django.contrib import messages
from users.mixins import LoginStaffMixin

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'registration/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido {username}!!!'
                }
                return render(request, 'index.html', context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Usuario o contraseña incorrectos!'
        }
        return render(request, 'registration/login.html', context=context)

def register(request):
    data={
        'form': RegisterForm()
    }
    if request.method == 'POST':
        register_form=RegisterForm(data=request.POST)

        if register_form.is_valid():
            register_form.save()
            user= authenticate(username=register_form.cleaned_data['username'], password=register_form.cleaned_data['password1'])
            login(request, user)
            return redirect(to="/")
    else:
        register_form=RegisterForm()
    return render(request, 'users/register.html', data)

@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm(initial = {
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_user.html', context=context)

    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return redirect('/')
        
        context = {
            'errors':form.errors,
            'form':UserUpdateForm()
        }
        return render(request, 'users/update_user.html', context=context)

@login_required
def update_user_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'birth_date':request.user.profile.birth_date,
            'profile_picture':request.user.profile.profile_picture
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('/')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/update_profile.html', context=context)

@login_required
def show_user(request):

    return render(request, 'users/show_user.html')


class UserList(LoginStaffMixin,ListView):

    model=User
    template_name= 'users/user_list.html'
    permission_required='perms.app.delete_user'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


def edit_user(request,id):
    user = User.objects.get(id=id)
    if request.method == 'GET':
        form=UserUpdateForm(instance=user)
    else:
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect(to ="/users/user_list/" )
    return render(request, 'users/update_user.html', {'form':form})
