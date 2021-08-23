from django.shortcuts import render

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

def formularioWebanimal(request):
    return render(request, 'formularioWebanimal.html',{
        #context 
    })

def formularioRegistro(request):
    return render(request, 'formularioRegistro.html',{
        #context 
    })

def Contactos(request):
    return render(request, 'ContactosWebanimal.html',{
        #context
    })

def InicioSesion(request):
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

