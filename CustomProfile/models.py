from django.db import models
from django.conf import settings
from django.utils import timezone


class UserProfile(models.Model):
    users=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_constraint=False,primary_key=True)
    image=models.ImageField(upload_to='upload',default="upload/user.png")
    bio=models.TextField(blank=True)
    date_register=models.DateField(default=timezone.now)
    


    
    class Meta:
        ordering=["-date_register"]


    def __str__(self) -> str:
        return self.users.username
