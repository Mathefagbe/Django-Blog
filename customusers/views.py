from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse
from .forms import CustomUserCreationform
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages


 

# Create your views here.
class SignUpView(CreateView):
    form_class=CustomUserCreationform
    template_name="signup.html"



    def get_success_url(self) -> str:
        return reverse("login")

class UserLogin(SuccessMessageMixin,LoginView):
    template_name="login.html"
    success_message="login successful"

    def get_success_url(self) -> str:
        return reverse("home")
 


