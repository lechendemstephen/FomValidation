from django.shortcuts import render # type: ignore
from .forms import ContactForm
from .models import Contacts
from django.contrib import messages # type: ignore
# Create your views here.

def contact(request): 
    if request.method == "POST": 
        form = ContactForm(request.POST)
        if form.is_valid():
           data = Contacts()
           data.email = form.cleaned_data['email']
           data.password = form.cleaned_data['password']
           data.address = form.cleaned_data['address']
           data.zip = form.cleaned_data['zip']
           data.save()
           messages.success(request, 'Thank you for contacting us')

    else: 
        form = ContactForm()


    return render(request, 'FormValidation/Forms/contact.html')
