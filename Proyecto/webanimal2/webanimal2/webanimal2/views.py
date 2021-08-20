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

