from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact-success/', views.contact_success_view, name='contact-success'),
]