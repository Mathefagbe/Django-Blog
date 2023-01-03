from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserProfile
from django.core.mail import send_mail

#this function will only be triggered when a new instance of user is created
# @receiver will listen for changes in the user after user is created.
 
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender,instance,created,**kwargs):
    if created:
        user_profile=UserProfile()
        user_profile.users=instance
        user_profile.save()
        send_mail(subject="ACCOUNT SUCCESSFULY CREATED"\
            ,message=f"Congratulations {instance.first_name} you have successfully created an account with DBlog"\
                ,from_email="fagbemi65@gmail.com"\
                    ,recipient_list=[f"{instance.email}"]\
                        ,fail_silently=False)
                        

        