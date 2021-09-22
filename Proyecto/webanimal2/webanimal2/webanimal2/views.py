from App1.models import User
from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html',{
        #context
        'message': 'Mensaje desde el contexto Django',
        'numero': [1,2,3,4,5],
    })

def Donaciones(request):
    return render(request, 'Donaciones.html',{
        #context 
    })

def frmadopcion(request):
    return render(request, 'formularioWebanimal.html',{
        #context 
    })

def register(request):
    return render(request, 'FormularioRegistro.html',{
        #context 
    })

def Contactos(request):
    return render(request, 'ContactosWebanimal.html',{
        #context
    })

def acceder(request):
    return render(request, 'InicioSesion.html',{
        #context
    })

def Nosotros(request):
    return render(request, 'Nosotros.html',{
        #context
    })

def Pagina_Inicio(request):
    return render(request, 'Pagina_Inicio.html',{
        #context
    })

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        email = authenticate(username=email, password=password)
        if email:
            login(request, email)
            messages.success(request, 'Bienvenido {}'.format(email.username))
            return redirect('Pagina_Inicio') # Nombre url
        else: 
            messages.error(request, 'Usuario o contraseña incorrecta')
    return render(request, 'InicioSesion.html',{
    })

#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            username = form.cleaned_data['username']
#            messages.success(request, f'Usuario {username} creado.')
#    else:
     #   form = UserCreationForm()

    #context = {'form : form'}
    #return render(request, 'templates/register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')



