from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .forms import RegisterForm
from django.contrib.auth.models import User
from pets.models import Pets


def index(request):
    # pets = Pets.objects.all().order_by('-id')
    return render(request, 'index.html',{
        # 'pets': pets,
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

def adopt(request):
    pets = Pets.objects.all().order_by('-id')
    return render(request, 'adopt.html',{
        'pets': pets,
        #context
    })

