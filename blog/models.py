import uuid
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.conf import settings
from CustomProfile.models import UserProfile
from tinymce import models as tinymce_models


# Create your models here.
class Post(models.Model):
    id=models.UUIDField(default=uuid.uuid4,editable=False ,primary_key=True)
    title=models.CharField(max_length=200)
    body=tinymce_models.HTMLField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,db_constraint=False)
    description=models.CharField(max_length=300)
    slug=models.SlugField( max_length= 200)
    updated=models.DateTimeField(auto_now=True)
    images=models.ImageField(upload_to='upload')
    author_profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True ,db_constraint=False)
    #likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="like",null=True)
    date_published=models.DateTimeField(default=timezone.now)
    


    class Meta:
        ordering=["-date_published"]
        



    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=100)
    comments=models.TextField(blank=True)
    date_commment=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=["-date_commment"]


    def __str__(self):
        return self.name




# # class Like(models.Model):
# #     likes=models.ForeignKey(Post,on_delete=models.CASCADE)
    



# #     def __str__(self) -> str:
# #         return self.likes