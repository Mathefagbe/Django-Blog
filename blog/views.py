from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from blog.mixin import UserProfileViewMixin
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.db.models import Q
from CustomProfile.models import UserProfile
from django.http import Http404, JsonResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostListView(UserProfileViewMixin,ListView):
    model=Post
    template_name="home.html"
    context_object_name="Posts"

    
    def get_queryset(self):
        return super().get_queryset()\
      .select_related('author','author_profile').all()


class TagPostList(UserProfileViewMixin,ListView):
    model=Post
    template_name='tag_post.html'
    context_object_name='Posts' 

    def get_queryset(self):
        return super().get_queryset()\
            .select_related('author','author_profile')\
            .filter(Q(slug__icontains=self.kwargs['tag_slug']) |Q(slug__istartswith=self.kwargs['tag_slug']))
      

class DetalsListView(FormMixin,UserProfileViewMixin,DetailView):
    model=Post
    template_name="details.html"
    context_object_name="post"
    form_class=CommentForm


    
    def get_object(self, queryset=None):
        queryset=self.model.objects\
            .select_related('author','author_profile')\
                .get(slug=self.kwargs["slug"])
        return queryset

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=Post.objects.get(slug=self.kwargs['slug'])
        context["comments"]=Comment.objects.filter(post=post)
        return context
    




class CreatePost(LoginRequiredMixin,UserProfileViewMixin,CreateView):
    model=Post
    login_url="signup"
    template_name="createpost.html"
    fields=["title","body","images","tag"]
    

    def form_valid(self, form):
        form.instance.author=self.request.user 
        user_profile=UserProfile.objects\
        .filter(users=self.request.user).first()
        form.instance.author_profile=user_profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("home")



class UpdatePost(UserProfileViewMixin,UpdateView):
        model=Post
        template_name="edit_post.html"
        fields=["title","body","images","tag"]


        def get_success_url(self) -> str:
            return reverse("home")





class ListOfUserPost(UserProfileViewMixin,ListView):
    model=Post
    template_name="allpost.html"
    context_object_name="Posts"

    def get_queryset(self):
        return super().get_queryset()\
        .select_related('author','author_profile')\
        .filter(author=self.request.user)


class CreateComment(CreateView):
    model=Comment
    form_class= CommentForm
   
    
    
    def form_valid(self, form):
        post_created=Post.objects.get(slug=self.kwargs["slug"])
        form.instance.post=post_created
        return super().form_valid(form) 

    def get_success_url(self):
        return reverse("details",kwargs={"slug":self.kwargs["slug"]})



def deletePostView(request):
    post_id=json.load(request)['id']
    Post.objects.filter(id=post_id).delete()
    return JsonResponse({"Post_id":post_id})


@ login_required
def likes(request):
    post_id=json.load(request)['id']
    get_post=get_object_or_404(Post,id=post_id)
    if get_post.likes.filter(id=request.user.id).exists():
        get_post.likes.remove(request.user) 
        get_post.like_count-=1
        get_post.save()
    else:
        get_post.likes.add(request.user)
        get_post.like_count+=1
        get_post.save()
    return JsonResponse({'total_like':get_post.like_count})