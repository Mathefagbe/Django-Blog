from django.views import View
from CustomProfile.models import UserProfile


class UserProfileViewMixin(View):
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context=super().get_context_data(**kwargs)
            context["userprofile"]=UserProfile.objects.filter(users=self.request.user).first()
            return context
        else:
            return super().get_context_data(**kwargs)