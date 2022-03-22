from django.shortcuts import render
from .forms import ContactsForm
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def contacts(request):
    form = ContactsForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            messages.success(request, "Asunto enviado exitosamente")
            return redirect('contacts')

    return render(request, 'contacts/contacts.html',{
        #context
        'form': form,
    }) 