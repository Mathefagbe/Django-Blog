
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.views import View
from CustomProfile.models import UserProfile
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
class UserProfileViewMixin(View):
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context=super().get_context_data(**kwargs)
            context["userprofile"]=UserProfile.objects.filter(users=self.request.user).first()
            return context
        else:
            return super().get_context_data(**kwargs)




class PostListView(UserProfileViewMixin,ListView):
    model=Post
    template_name="home.html"
    context_object_name="Posts"





class DetalsListView(FormMixin,UserProfileViewMixin,DetailView,):
    queryset=Post.objects.all()
    template_name="details.html"
    context_object_name="post"
    form_class=CommentForm


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        Post_Object=Post.objects.get(id=self.kwargs["pk"])
        context["comments"]=Comment.objects.filter(post=Post_Object)
        return context
    




class CreatePost(LoginRequiredMixin,UserProfileViewMixin,CreateView):
    model=Post
    login_url="signup"
    template_name="createpost.html"
    fields=["title","body","images"]
    

    

    def form_valid(self, form):
        form.instance.author=self.request.user 
        user_profile=UserProfile.objects.filter(users=self.request.user).first()
        form.instance.author_profile=user_profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("home")



class UpdatePost(UserProfileViewMixin,UpdateView):
        model=Post
        template_name="edit_post.html"
        fields=["title","body","images"]


        def get_success_url(self) -> str:
            return reverse("home")



class DeletePost(UserProfileViewMixin,DeleteView):
    model=Post
    template_name="delete.html"
    context_object_name="post"



    def get_success_url(self) -> str:
        return reverse_lazy("home")




class LIST_OF_USER_POST(UserProfileViewMixin,ListView):
    template_name="allpost.html"
    context_object_name="Posts"


    def get_queryset(self):
        userpost=Post.objects.filter(author=self.request.user)
        return userpost



class CreateComment(CreateView):
    model=Comment
    form_class= CommentForm
   
    
    
    def form_valid(self, form):
        Post_Object=Post.objects.get(id=self.kwargs["pk"])
        form.instance.post=Post_Object
        return super().form_valid(form) 

    def get_success_url(self):
        return reverse("details",kwargs={"pk":self.kwargs["pk"]})




    
#Test view
@csrf_exempt
def ajax_get_view(request):
    # das=json.load(request)['post_data']
    # print(das)
    
    # print(dats[1].title)
    data={
        "sucess":"pass"
    }
    return JsonResponse(data)