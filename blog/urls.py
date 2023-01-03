from django.urls import path
from .views import (PostListView,
DetalsListView,
CreateComment, 
CreatePost,
ListOfUserPost,
UpdatePost,
deletePostView,
TagPostList,
likes)

urlpatterns = [
    path("home/",PostListView.as_view(),name="home"),
    path("tag/<slug:tag_slug>",TagPostList.as_view(),name="tag"),
    path("details/<slug:slug>/", DetalsListView.as_view(),name="details"),
    path("comment/<slug:slug>/", CreateComment.as_view(),name="comment"),
    path("new_post/",CreatePost.as_view(),name="newpost"),
    path("user_post/", ListOfUserPost.as_view(), name="userpost"),
    path("edit_post/<slug:slug>/",UpdatePost.as_view(), name="editpost" ),
    path("delete/",deletePostView),
    path("likes/",likes)

]
# slug can also ne used as url path in ur url