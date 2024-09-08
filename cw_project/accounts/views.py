from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

#Handles user registration
class Register(CreateView):
    #Uses Django's UserCreationForm to create a user
    form_class = UserCreationForm 
    #Tells the program to redirect to the login page once a user has been created
    success_url = reverse_lazy("login")
    #Links the template for the registration page
    template_name = "registration/register.html"

