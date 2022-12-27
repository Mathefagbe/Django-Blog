from django.apps import AppConfig


class CustomprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CustomProfile'

    def ready(self):
        from . import signals
    #     # return super().ready()
