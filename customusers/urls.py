from django.urls import path
from .views import SignUpView,UserLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("signup/",SignUpView.as_view(), name="Register"),
    path("login/",UserLogin.as_view(), name="login"),
    path("logout/",LogoutView.as_view(template_name="logout.html",next_page="login"), name="logout"),
]