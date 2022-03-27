from tkinter import S
from django.shortcuts import render
from .forms import AdoptionForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def frmAdoption(request):
    form = AdoptionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            messages.success(request, "Asunto enviado exitosamente")
            return redirect('Adoption')


    return render(request, 'Adoption.html',{
        'form': form
    })