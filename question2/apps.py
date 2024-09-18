from django.apps import AppConfig


class Question2Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "question2"
    
    def ready(self):
        from . import signals
