from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
