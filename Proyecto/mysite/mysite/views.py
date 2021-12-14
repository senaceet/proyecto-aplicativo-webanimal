from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .forms import RegisterForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html',{
        #context
        
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect ('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienevenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña inválido')
    return render(request, 'users/login.html', {
        #
    })

def logout_view(request):
        logout(request)
        messages.success(request, 'Sesión Cerrada')
        return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect ('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form' : form 
    })

def aboutUs(request):
    return render(request, 'aboutUs.html',{
        #context
    })

def contacts(request):
    return render(request, 'contacts.html',{
        #context
    }) 

def donation(request):
    return render(request, '../templates/donation/donation.html',{
        #context
    })

def frmDonation(request):
    return render(request, '../templates/donation/frmDonation.html',{
        #context
    })

def news(request):
    return render(request, 'news.html',{
        #context
    })

