from .models import UserProfile
from django import forms


class ProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=["image","bio"]