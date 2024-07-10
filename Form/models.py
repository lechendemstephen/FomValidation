from django.db import models # type: ignore

# Create your models here.

class Contacts(models.Model): 
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
    jioned_date = models.DateTimeField(auto_now_add=True)


    def __str__(self): 

        return self.email

    class Meta: 
        verbose_name = 'Contacts' 
        verbose_name_plural = 'Contacts'
    
