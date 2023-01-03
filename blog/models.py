import uuid
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.conf import settings
from CustomProfile.models import UserProfile
from tinymce import models as tinymce_models
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager



# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    body=tinymce_models.HTMLField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,db_constraint=False)
    slug=models.SlugField(max_length= 200,unique=True)
    updated=models.DateTimeField(auto_now=True)
    images=models.ImageField(upload_to='upload')
    author_profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True ,db_constraint=False)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="like",default=None ,blank=True)
    like_count=models.BigIntegerField(default="0")
    date_published=models.DateTimeField(default=timezone.now)
    tag=TaggableManager()


    class Meta:
        ordering=["-date_published"]
        indexes=[
            models.Index(fields=['-date_published','slug'])
        ]
        
    def __str__(self) -> str:
        return self.title

        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super().save(*args,**kwargs)


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=100)
    comments=models.TextField(blank=True)
    date_commment=models.DateTimeField(default=timezone.now)
    


    class Meta:
        ordering=["-date_commment"]


    def __str__(self):
        return self.name
