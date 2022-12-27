from django.urls import path
from .views import (PostListView,
DetalsListView,
CreateComment, 
CreatePost,
LIST_OF_USER_POST,
UpdatePost,DeletePost,
ajax_get_view)

urlpatterns = [
    path("home/",PostListView.as_view(),name="home"),
    path("details/<str:pk>/", DetalsListView.as_view(),name="details"),
    path("comment/<str:pk>/", CreateComment.as_view(),name="comment"),
    path("new_post/",CreatePost.as_view(),name="newpost"),
    path("user_post/", LIST_OF_USER_POST.as_view(), name="userpost"),
    path("edit_post/<str:pk>/",UpdatePost.as_view(), name="editpost" ),
    path("delete/<str:pk>/",DeletePost.as_view(),name="deletePost"),
    path("test/",ajax_get_view,name="ajaxview")

]
# slug can also ne used as url path in ur url