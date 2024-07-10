from django.contrib import admin # type: ignore
from .models import Contacts
# Register your models here.

class ContactsAdmin(admin.ModelAdmin): 
    list_display = ('email', 'password', 'address', 'city', 'zip', 'jioned_date')


admin.site.register(Contacts, ContactsAdmin)