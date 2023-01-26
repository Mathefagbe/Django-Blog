from django.shortcuts import render
from django.urls import reverse
from .models import UserProfile
from django.views import generic
from blog.models import Post
from blog.mixin import UserProfileViewMixin
from .forms import ProfileForm



class UserProfileview(UserProfileViewMixin,generic.ListView):
    model=UserProfile
    template_name="profile.html"
    context_object_name="profiles"

    def get_queryset(self):
        user_profile=super().get_queryset()
        user_profile=self.model.objects.filter(users=self.request.user).first()
        return user_profile




class UpdateUserProfile(UserProfileViewMixin, generic.UpdateView):
    model=UserProfile
    form_class=ProfileForm
    template_name="editprofile.html"


    def get_success_url(self) -> str:
        return reverse("profile")
    
    
  





