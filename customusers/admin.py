from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users
from .forms import CustomUserCreationform, CustomUserChangeForm


# Register your models here.
class CustomAdmin(UserAdmin):
    add_form=CustomUserCreationform
    form=CustomUserChangeForm
    model=Users
    list_display = ['email', 'username', 'is_staff', ]


admin.site.register(Users,CustomAdmin)