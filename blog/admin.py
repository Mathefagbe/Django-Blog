from django.contrib import admin
from .models import Comment,Post 


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=["id","title","author","updated","date_published"]
    prepopulated_fields={"slug":["title"]}
    search_fields=["title"]
  

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
