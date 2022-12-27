from django.urls import path
from .views import UserProfileview,UpdateUserProfile


urlpatterns = [
    path("profile/",UserProfileview.as_view(),name="profile"),
    path("edit_profile/<int:pk>/",UpdateUserProfile.as_view(),name="edit_profile")
]