import email
from tkinter import S
from django.shortcuts import render, redirect
from .forms import AdoptionForm
from django.contrib import messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings




# Create your views here.
def frmAdoption(request):
    form = AdoptionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            messages.success(request, "Asunto enviado exitosamente, te estaremos contactando!!")
            return redirect('Adoption')

    return render(request, 'Adoption.html',{
        'form': form
    })
    

def email(request):
    if request.method == 'POST':
        email = request.POST.get('Correo')
        print(email)

    template = render_to_string('Correo.html',{
        'email': email,
    })

    email = EmailMessage(
        template,
        settings.EMAIL_HOST_USER,
        ['sebatan4@gmail.com']
    )

    email.fail_silently = False
    email.send()

    

