from django import forms  # type: ignore
from .models import Contacts

class ContactForm(forms.ModelForm): 
    class Meta: 
        model = Contacts
        fields = ['email', 'password', 'address', 'city', 'zip']
    
    
