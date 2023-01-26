
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ValidationError
from .models import Users
from django import forms


class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Users
        fields=['username', 'email','first_name',]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2
    def clean_email(self):
        print("hello")
        data = self.cleaned_data['email']
        if Users.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data
        
        
    


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=Users
        fields=['username', 'email','first_name',]
        