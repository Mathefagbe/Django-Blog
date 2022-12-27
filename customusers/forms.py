
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Users


class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Users
        fields=['username', 'email','first_name',]
        
        



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=Users
        fields=['username', 'email','first_name',]
        